from canva import templates
from canva import cadastrar_template


def test_cadastar_template ():
   assert len(templates) == 0
   assert cadastrar_template("meu template 3", "amarelo", "tema 2" ) == True
   assert len(templates) == 1
   assert cadastrar_template("", "amarelo", "tema 2" ) == False
   assert len(templates) == 1
   
 #def ()
# def test_soma():
#    assert soma(5,6) == 11