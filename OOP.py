from enum import Enum

class Affiliation(Enum):
    REBEL_ALLIANCE = 0
    GALACTIC_EMPIRE = 1
    UNKNOWN = 2

# Clase PADRE
class StarWarsCharacter:
    def __init__(self, name, alias, affiliation):
        """
        Crea un personaje con nombre y alias
        """
        self.name = name
        self.alias = alias
        self.affiliation = affiliation
        
    def __repr__(self):
        """
        Muestra una representación textual del objeto
        """
        return f'<{self.__class__}: {self.name} {self.alias}>'

# Subclase de StarWarsCharacter: ForceSensitive
class ForceSensitive(StarWarsCharacter):
    """
    Representa personajes sensibles a la Fuerza
    """
    def __init__(self, name, alias, affiliation, midichlorians):
        super().__init__(name, alias, affiliation)
        self.midichlorians = midichlorians
        
    def unsheathe(self):
        """
        Este método, solo sirve para que mis subclases lo entiendan y no tenga que repetirlo
        """
        raise NotImplementedError()

# Subclase de ForceSensitive: Jedi
class Jedi(ForceSensitive):
    
    @classmethod # Modificador que transforma el método en un método de clase
    # Los métodos de clase se suelen utilizar como formas especializadas de comprar instancias
    def master (cls, name, alias):
        """ 
        Crea un maestro jedi (con 100k midiclorianos)
        """
        return cls (name, alias, 100000)

    @classmethod
    def padawan (cls, name, alias):
        return cls (name, alias, 10)

    def __init__(self, name, alias, midichlorians):
        super().__init__(name, alias, Affiliation.REBEL_ALLIANCE, midichlorians)
        
    def unsheathe(self):
        return '▐▍░▐░░▣░▒░▒░▒▕|' + "█" * 40

# Subclase de ForceSensitive: Sith
class Sith(ForceSensitive):

    @classmethod
    def darkLord (cls, name, alias):
        return  cls(name, alias, 120000)

    def __init__(self, name, alias, midichlorians):
        super().__init__(name, alias, Affiliation.GALACTIC_EMPIRE, midichlorians)
        
    def unsheathe(self):
        return '▔▔▔▔▔▔▔▔▔▝▔▔▔ ' + "█" * 40
