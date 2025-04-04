```mermaid
graph TD;
    
    %% External Entities
    User["User"] -->|View Products| PDB["Product Database"];
    User -->|Add/Remove Products| Cart["Shopping Cart"];
    User -->|Checkout| Order["Order Processing"];

    %% Product Management
    PDB -->|Fetch Products| Display["Display Products"];
    Display -->|Show Products| User;
    Cart -->|Check Stock| PDB;
    
    %% Cart Management
    Cart -->|Update Cart| CartData["Cart Data"];
    User -->|View Cart| Cart;
    
    %% Checkout Process
    Order -->|Calculate Total| Total["Total Price"];
    Total -->|Select Payment Method| Payment["Payment Gateway"];
    Payment -->|Process Payment| PG["Payment Processor"];
    PG -->|Confirm Payment| Order;
    Order -->|Update Order Data| ODB["Order Database"];
    Order -->|Clear Cart| Cart;
    
    %% Data Stores
    PDB -.->|Stores| ProductDB["Product Database"];
    CartData -.->|Stores| CartDB["Cart Data"];
    ODB -.->|Stores| OrderDB["Order Data"];
