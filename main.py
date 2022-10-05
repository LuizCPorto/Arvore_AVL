from ast import Return
from calendar import c
from importlib.resources import contents
from logging import root
from msilib.schema import SelfReg
from multiprocessing.sharedctypes import Value
from operator import truediv
from threading import currentThread
from tkinter import N
from typing_extensions import Self
from xml.dom import minicompat
import no

class AVLTree:
    def __init__(self):
        self.root=None
    
    def __repr__(self):
        if self.root==None: return ''
        content='\n'
        cur_nos=[self.root]
        cur_alturas=self.root.altura
        sep=' '*(2**(cur_alturas-1))
        while True:
            cur_alturas+=-1
            if len(cur_nos)==0: break
            cur_fila=' '
            proxima_fila=''
            proximo_no=[]

            if all(n is None for n in cur_nos):
                break
            for n in cur_nos:

                if n==None:
                    cur_fila+='  '+sep
                    proxima_fila+='  '+sep
                    proximo_no.extend([None,None])
                    continue

                if n.value!=None:
                    buf=' '*((5-len(str(n.value)))/2)
                    cur_fila+='%s%s%s'%(buf,str(n.value),buf)+sep
                else:
                    cur_fila+=' '*5+sep
                
                if n.filho_esquerda!=None:
                    proximo_no.append(n.filho_esquerda)
                    proxima_fila+=' /'+sep
                else:
                    proxima_fila+=' '+sep
                    proximo_no.append(None)

                if n.filho_direita!=None:
                    proximo_no.append(n.filho_direita)
                    proxima_fila+='\ '+sep
                else:
                    proxima_fila+=' '+sep
                    proximo_no.append(None)
            
            content+=(cur_alturas*'  '+cur_fila+'\n'+cur_alturas*'  '+proxima_fila+'\n')
            cur_nos=proximo_no
            sep=' '*(len(sep)/2)
        return content

    def inserir(self,value):
        if self.root==None:
            self.root=no(value)
        else: 
            self._inserir_(value, self.root)

    def _inserir_(self,value,cur_no):
        if value<cur_no.value:
            if cur_no.filho_esquerda==None:
                cur_no.filho_esquerda=no(value)
                cur_no.filho_esquerda.pai=cur_no
                self._inspect_insertion(cur_no.filho_esquerda)
            else:
                self._inserir_(value, cur_no.filho_esquerda)
        elif value>cur_no.value:
            if cur_no.filho_direita==None:
                cur_no.filho_direita=no(value)
                cur_no.filho_direita.pai=cur_no
                self._inspect_insertion(cur_no.filho_direita)
            else:
                self._inserir_(value, cur_no.filho_direita)
        else:
            print ('Valor já adcionado na arvore')
    
    def print(self):
        if self.root!=None:
            self._print_(self, root)

    def _print_ (self,cur_no):
        if cur_no!=None:
            self._print_(cur_no.filho_esquerda)
            print ('%s, h=%d'%(str(cur_no.value),cur_no.altura))
            self._print_(cur_no.filho_direita)
    
    def altura(self):
        if self.root!=None:
            return self._altura_(self.root, 0)
        else: 
            return 0
    
    def _altura_(self,cur_no,cur_altura):
        if cur_no==None: return cur_altura
        altura_esquerda=self._altura_(cur_no.filho_esquerda,cur_altura+1)
        altura_direita=self._altura_(cur_no.filho_direita,cur_altura+1)
        return max(altura_esquerda, altura_direita)

    def busca(self,value):
        if self.root!=None:
            return self._busca_(value, self.root)
        else:
            return None

    def _busca_(self,value,cur_no):
        if value==cur_no.value:
            return cur_no
        elif value<cur_no.value and cur_no.filho_esqueda!=None:
            return self._busca_(value,cur_no.filho_esquerda)
        elif value>cur_no.value and cur_no.filho_direita!=None:
            return self._busca_(value,cur_no.filho_direita)
    
    def apagar_valor(self, value):
        return self.apagar_no(self.busca(value))

    def apagar_no(self,no):
        if no==None or self.busca(no.value)==None:
            print ('Não foi possivel excluir o Nó, poís não foi encontrado!')
            return None
    
    def minino(n):
        current=n
        while current.filho_esquerda!=None:
            current=current.filho_esquerda
        return current
    
    def numeros_filhos(n):
        numeros_filhos=0
        if n.filho_esquerda!=None: numeros_filhos+=1
        if n.filho_direita!=None: numeros_filhos+=1
        return numeros_filhos

no_pai=no.pai

no_filho=numeros_filhos(no)

if no_filho==0:
    if no_pai!=None:
        no_pai.filho_esquerda=None
    else:
       no_pai.filho_direita=None
else:
   Self.root=None

if  no_filho==1:
    if no.filho_esquerda!=None:
        filho=no.filho_esquerda
    else:
        filho=no.filho_direita

    if no_pai!=None:
        if no_pai.filho_esquerda==no:
            no_pai.filho_esquerda=filho
        else:
            no_pai.filho_direita=filho
    else:
        self.root=filho

    filho.pai=no_pai

if no_filho==2:
    sucessor=minicompat(no.filho_direita)

    no.value=sucessor.value

    SelfReg.apagar_no(sucessor)

    Return
    
if no_pai!=None:
    no_pai.altura=+1+max(self.get_altura(no_pai.filho_esquerda),self.get_altura(no_pai.filho_direita))

    self._verifica_apagar_(no_pai)    

    def procura(self,value):
        if self.root!=None:
            return self._procura_(value,self.root)
        else: 
            return False

    def _procura_(self,value,cur_no):
        if value==cur_no.value:
            return True
        elif value<cur_no.value and cur_no.filho_esquerda!=None:
            return self._procura_(value,cur_no.filho_esquerda)
        elif value>cur_no.value and cur_no.filho_direita!=None:
            return self._procura_(value,cur_no.filho_direita)
        return False

    def _verifica_inserir_(self,cur_no,path):
        if cur_no.pai==None: return
        path=[cur_no]+path

        altura_esquerda =self.get_altura(cur_no.pai.filho_esquerda)
        altura_direita =self.get_altura(cur_no.pai.filho_direita)

        if abs(altura_esquerda-altura_direita)>1:
            path[cur_no.pai]+path 
            self._rebalaceamento_no_(path[0],path[1],path[2])
            return

        nova_altura=1+cur_no.altura
        if nova_altura>cur_no.pai.altura:
            cur_no.pai.altura=nova_altura

        self._verifica_inserir_(cur_no.pai,path)


    def _verifica_apagar_(self,cur_no):
        if cur_no==None: return

        altura_esquerda =self.get_altura(cur_no.filho_esquerda)
        altura_direita =self.get_altura(cur_no.filho_direita)

        if abs(altura_esquerda-altura_direita)>1:
            y=self.maior_filho(cur_no)
            x=self.maior_filho(y)
            self._rebalaceamento_no_(cur_no,y,x)

        self._verifica_apagar_(cur_no.pai)

    def _rebalaceamento_no_(self,z,y,x):
        if y==z.filho_esquerda and x==y.filho_esquerda:
            self._rodar_direita(z)
        elif y==z.filho_esquerda and x==y.filho_direita:
                self._rodar_esquerda(y)
                self._rodar_direita(z)
        elif y==z.filho_direita and x==y.filho_direita:
                self._rodar_esquerda(z)
        elif y==z.filho_direita and x==y.filho_esquerda:
                self._rodar_direita(y)
                self._rodar_direita(z)
        else:
            raise Exception('_rebalaceamenti_no: configuração de nó z,y,x não reconhecida!')

    def _rodar_direita(self,z):
        sub_root=z.pai
        y=z.filho_esquerda
        t3=y.filho_direita
        y.filho_direita=z
        z.pai=y
        z.filho_esquerda=t3
        if t3!=None: t3.pai=z
        y.pai=sub_root
        if y.pai==None:
            self.root=y
        else:
            if y.pai.filho_esquerda==z:
                y.pai.filho_esquerda=y
            else: 
                y.pai.filho_direita=y
        z.altura=1+max(self.get_altura(z.filho_esquerda),
            self.get_altura(z.filho_direita))
        y.altura=1+max(self.get_altura(y.filho_esquerda),
            self.get_altura(y.filho_direita))
    
    def _rodar_esquerda(self,z):
        sub_root=z.pai
        y=z.filho_direita
        t2=y.filho_esquerda
        y.filho_esquerda=z
        z.pai=y
        z.filho_direita=t2
        if t2!=None: t2.pai=z
        y.pai=sub_root
        if y.pai==None:
            self.root=y
        else:
            if y.pai.filho_esquerda==z:
                y.pai.filho_esquerda=y
            else: 
                y.pai.filho_direita=y
        z.altura=1+max(self.get_altura(z.filho_esquerda),
            self.get_altura(z.filho_direita))
        y.altura=1+max(self.get_altura(y.filho_esquerda),
            self.get_altura(y.filho_direita))
        
    def get_altura(self,cur_no):
        if cur_no==None: return 0
        return cur_no.altura

    def maior_filho(self,cur_no):
        esquerda=self.get_altura(cur_no.filho_esquerda)
        direita=self.get_altura(cur_no.filho_direita)
        return cur_no.filho_esquerda if esquerda>=direita else cur_no.filho_direita


a=AVLTree()
for i in range(10):
    print ('INSERRINDO %d'%i)
    a.inserir(i)
    print (a)
for i in range(10):
    print ('Deletando %d'%i)
    a.apagar_valor(i)
    print (a)
