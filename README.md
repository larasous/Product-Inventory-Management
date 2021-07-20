# Product-Inventory-Management
O system allows you to perform the following operations: register, list, search, update and remove products.

## Goals

1. Use the knowledge covered in composite structures: lists, dictionaries
and tuples.
2. Organization of code into functions.


## System
The user, when running your program will have a menu of options like the following:

-----------------------
[ C ] Cadastrar

[ L ] Listar

[ B ] Buscar

[ A ] Atualizar

[ R ] Remover

[ S ] Sair

Escolha uma operação:

----------------------
After choosing to register, the information of a product is requested from the user by the system. A restriction on registration is: cannot register a product already registered, each product is unique in the system.

If the user has chosen option L, to list the products, a menu informing the user of listing options: by product name and by the amount.

If the user has chosen option B, to search for the products, the system will ask the user who informs the type of search: whether by product name or by its the amount.

Search by name if the product is registered, the user is informed of the name and the existing quantity of the product. If the product is not registered, the message "O product is unavailable.”. If the product is sought by quantity, the system shows all products that have a quantity equal to or greater than the amount informed by the user. This function differs from list because the function list searches all, and the search function does not, it filters what the user wants.

Option A, to update, asks the user to enter the product name so that update its quantity in stock. It is only possible to update if the product exists in stock.

The remove option, on the other hand, is similar to updating, in order to remove a product. Removal can only be performed if the product is available on the
stock.

In the LBAR options, if the product is out of stock, inform the user by the message “The product is unavailable”.
