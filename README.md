
---
- **EventBridge** routes `custom.invoice` and `custom.payment` events to respective Lambda functions.
- **Lambda Functions** process and store event data in DynamoDB tables.
- **DynamoDB Tables** (`InvoiceTable`, `PaymentTable`) store processed event data.
- **CloudFormation** used for Infrastructure as Code (IaC).
---
