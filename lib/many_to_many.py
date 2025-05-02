class Author:
    all_authors = []  # To keep track of all authors
    
    def __init__(self, name):
        self.name = name
        self._contracts = []  # To track related contracts for this author
        Author.all_authors.append(self)
    
    def contracts(self):
        """Returns the list of contracts related to the author."""
        return self._contracts
    
    def books(self):
        """Returns the list of books related to the author using the Contract class."""
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        """Creates and returns a new Contract between the author and book."""
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)  # Add contract to author's contracts
        return contract
    
    def total_royalties(self):
        """Returns the total royalties for the author."""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []  # To keep track of all books
    
    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)
    
    def contracts(self):
        """Returns the list of contracts related to the book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]
    
    def authors(self):
        """Returns a list of authors associated with the book."""
        return [contract.author for contract in Contract.all_contracts if contract.book == self]


class Contract:
    all_contracts = []  # To keep track of all contracts
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts with the specified date."""
        return sorted(
            [contract for contract in cls.all_contracts if contract.date == date],
            key=lambda contract: contract.date
        )
