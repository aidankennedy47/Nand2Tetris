from ParseTree import *

class CompilerParser :

    def __init__(self,tokens):
        self.tokens = tokens
        self.current_token_index = 0
        pass
    

    def compileProgram(self):
        """
        Generates a parse tree for a single program
        @return a ParseTree that represents the program
        """
        if not self.tokens:
            raise ParseException("No tokens to parse")
        
        if self.have('keyword', 'class'):
            return self.compileClass()
        else:
            raise ParseException("The program does not begin with keyword class")
    
    
    def compileClass(self):
        """
        Generates a parse tree for a single class
        @return a ParseTree that represents a class
        """
        if not self.have('keyword', 'class'):
            raise ParseException("The program does not begin with a class!")
        
        class_tree = ParseTree('class', '')
        class_tree.addChild(self.mustBe('keyword', 'class'))

        class_name = self.current().getValue()

        class_tree.addChild(self.mustBe('identifier', class_name))

        class_tree.addChild(self.mustBe('symbol', '{'))

        VarDec = self.compileClassVarDec()
        while VarDec is not None:
            class_tree.addChild(VarDec)
            VarDec = self.compileClassVarDec()

        Subroutine = self.compileSubroutine()
        while Subroutine is not None:
            class_tree.addChild(Subroutine)
            Subroutine = self.compileSubroutine()

        class_tree.addChild(self.mustBe('symbol', '}'))

        return class_tree
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """
        return None 
    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        return None 
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        return None 
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        return None 
    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """
        return None 
    

    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """
        return None 
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        return None 

    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        return None 


    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        return None 


    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        return None 


    def next(self):
        self.current_token_index += 1
        return


    def current(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        else:
             raise ParseException("No more tokens to parse!")


    def have(self,expectedType,expectedValue):
        current_token = self.current()
        if current_token.getType() == expectedType and current_token.getValue() == expectedValue:
            return True
        elif current_token.getType() == expectedType and current_token.getValue() in expectedValue:
            return True
        return False


    def mustBe(self,expectedType,expectedValue):
        current_token = self.current()
        if self.have(expectedType, expectedValue):
            self.next()
            return current_token
        else:
            raise ParseException("Expected type or value does not match!")
    

if __name__ == "__main__":


    """ 
    Tokens for:
        class MyClass {
        
        }
    """
    tokens = []
    tokens.append(Token("keyword","class"))
    tokens.append(Token("identifier","MyClass"))
    tokens.append(Token("symbol","{"))
    tokens.append(Token("symbol","}"))

    parser = CompilerParser(tokens)
    try:
        result = parser.compileProgram()
        print(result)
    except ParseException:
        print("Error Parsing!")
