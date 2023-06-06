class Equivalence:
    
    @classmethod
    def check_transitive(cls, R):
      for i in R:
        for j in R:
          if i[1] == j[0]:
            if (i[0],j[1]) not in R:
              return False
      return True

    @classmethod
    def check_symmetric(cls, R):
      for i in R:
        if (i[1],i[0]) not in R:
          return False
      return True

    @classmethod
    def check_reflexive(cls, R):
      for i in R:
        for j in i:
          if (j,j) not in R:
            return False
      return True

    @classmethod
    def check(cls,R):
      if not equivalence.check_transitive(R) and equivalence.check_symmetric(R) and equivalence.check_reflexive(R):
        return False
      return True
