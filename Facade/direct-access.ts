class EmailService {
  sendEmail(to: string, subject: string, body: string) {
    console.log(`Enviando correo a ${to}: "${subject}"`);
  }
}

class PDFGenerator {
  generate(data: any) {
    console.log("Generando PDF con datos:", data);
    return "ruta/del/reporte.pdf";
  }
}

class Logger {
  log(message: string) {
    console.log("LOG:", message);
  }
}

function clienteGeneraReporte() {
  const email = new EmailService();
  const pdf = new PDFGenerator();
  const logger = new Logger();

  logger.log("Inicio del proceso de reporte");
  const pdfPath = pdf.generate({ ventas: 1000, sucursal: "Coatzacoalcos" });
  email.sendEmail(
    "admin@empresa.com",
    "Reporte de Ventas",
    `Adjunto: ${pdfPath}`
  );
  logger.log("Reporte enviado.");
}

clienteGeneraReporte();
