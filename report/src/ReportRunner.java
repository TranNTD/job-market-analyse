// import java standard library
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.util.List;

// import BIRT jars library => java needs -cp to find them
import org.eclipse.birt.core.framework.Platform;
import org.eclipse.birt.report.engine.api.EngineConfig;
import org.eclipse.birt.report.engine.api.IReportEngine;
import org.eclipse.birt.report.engine.api.IReportEngineFactory;
import org.eclipse.birt.report.engine.api.IReportRunnable;
import org.eclipse.birt.report.engine.api.IRunAndRenderTask;
// import org.eclipse.birt.report.engine.api.PDFRenderOption;
import org.eclipse.birt.report.engine.api.RenderOption;

public class ReportRunner {

    public static void main(String[] args) throws Exception {
        // 0. Check the format, default is "pdf"
        String format = args.length > 0 ? args[0].toLowerCase(): "pdf";
        if (!format.equals("pdf") && !format.equals("pptx")){
            System.err.println("Unknow format: " + format + " (allowed: pdf, pptx)");
            System.exit(2);
        }
        // 1. Set Design and Output-path
        String design = "report/top_skills.rptdesign";
        Path outputDir = Path.of("report", "output");
        Files.createDirectories(outputDir); // create output folder if not exists
        Path output = outputDir.resolve("top_skills_" + LocalDate.now() + "."+format);

        // 2. Start BIRT: BIRT Setup -> Load Design and Create task -> Task's Output setup-option -> Run task
        // Fixed BIRT setup code: Config, Platform, Factory und Engine
        EngineConfig config = new EngineConfig();
        Platform.startup(config);
        IReportEngineFactory factory = (IReportEngineFactory) Platform.createFactoryObject(
                                        IReportEngineFactory.EXTENSION_REPORT_ENGINE_FACTORY);
        IReportEngine engine = factory.createReportEngine(config);

        try {
            // 3. Load the design and create a task that runs it and renders the result by Engine
            IReportRunnable report = engine.openReportDesign(design);
            IRunAndRenderTask task = engine.createRunAndRenderTask(report);

            // 4. Extensions: Format is read from args[0], "pdf" as default, only "pdf" and "pptx" allowed
            // PDFRenderOption options = new PDFRenderOption();  // General Render option for both formats
            RenderOption options = new RenderOption();
            options.setOutputFormat(format);
            options.setOutputFileName(output.toString());
            task.setRenderOption(options);

            // 5. Run: BIRT queries PostgreSQL and writes the output
            task.run();

            List<?> errors = task.getErrors();
            task.close();

            if (!errors.isEmpty()) {
                System.err.println("Report finished with errors:");
                errors.forEach(e -> System.err.println("  " + e));
                System.exit(1);
            }
            System.out.println("Report written: " + output);

        } finally {
            // 6. Shut BIRT down cleanly, even if something went wrong
            engine.destroy();
            Platform.shutdown();
        }
    }
}