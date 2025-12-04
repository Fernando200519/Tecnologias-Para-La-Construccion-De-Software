class EmailService {
  sendEmail(to: string, subject: string, body: string) {
    console.log(`Correo enviado a ${to}: "${subject}"`);
  }
}

class PDFGenerator {
  generate(data: any) {
    console.log("PDF generado con datos:", data);
    return "ruta/del/reporte.pdf";
  }
}

class Logger {
  log(message: string) {
    console.log("LOG:", message);
  }
}

class ReportFacade {
  private email = new EmailService();
  private pdf = new PDFGenerator();
  private logger = new Logger();

  generarYEnviarReporte(datos: any, destinatario: string) {
    this.logger.log("Inicio del proceso de reporte");

    const pdfPath = this.pdf.generate(datos);

    this.email.sendEmail(
      destinatario,
      "Reporte de Ventas",
      `Aquí tienes el reporte generado: ${pdfPath}`
    );

    this.logger.log("Reporte enviado correctamente");
  }
}

const reportFacade = new ReportFacade();
reportFacade.generarYEnviarReporte(
  { ventas: 1500, sucursal: "Coatzacoalcos" },
  "admin@empresa.com"
);
