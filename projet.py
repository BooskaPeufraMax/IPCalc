import ipaddress
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from ipaddress import *



root = tk.Tk()
style = ttk.Style(root)
notebook = ttk.Notebook(root)
f1 = tk.Frame(notebook, width=450, height=500)
f2 = tk.Frame(notebook, width=450, height=500)
f3 = tk.Frame(notebook, width=450, height=500)
notebook.add(f1, text="Calculateur de Masque")
notebook.add(f2, text="Calcalateur de Sous-Reseaux")
notebook.add(f3, text="Convertisseur")
notebook.grid(row=0, column=0, sticky="nw")
root.wm_title("Projet")
root.geometry("450x500")
#ip_address = str(ip1)+ "." +str(ip2) + "." + str(ip3) + "." + str(ip4)

def _dec_to_binary(ip_address):
    return map(lambda x: bin(x)[2:].zfill(8), ip_address)


def _negation_mask(net_mask):
    wild = list()
    for i in net_mask:
        wild.append(255 - int(i))
    return wild


class IPCalculator(object):
    def __init__(self, ip_address):
        if '/' in ip_address:
            self._address = map(int, self._address_val.split('.'))
        else:
            self._address = map(int, ip_address.split('.'))
            self.binary_IP = _dec_to_binary(self._address)
            self.binary_Mask = None
            self.negation_Mask = None
            self.network = None
            self.broadcast = None
            # if svRadio2.get() == 5 :
            #     self._cidr = entreeCIDR2.get()

    def __repr__(self):
        # print ("Calculating the IP range of %s/%s") % (".".join(map(str, self._address)), self._cidr)
        print ("==================================")
        # print ("Netmask %s") % (".".join(map(str, self.net_mask())))
        # print ("Network ID %s") % (".".join(map(str, self.network_ip())))
        print ("Subnet Broadcast address " + (".".join(map(str, self.broadcast_ip()))))
        # print ("Host range %s") % (self.host_range())

    # def net_mask(self):
    #     mask = [entreeMasque5.get(), entreeMasque6.get(), entreeMasque7.get(), entreeMasque8.get()]
    #     # for i in range(int(self._cidr)):
    #     #     mask[i / 8] += 1 << (7 - i % 8)
    #     self.binary_Mask = _dec_to_binary(mask)
    #     self.negation_Mask = _dec_to_binary(_negation_mask(mask))
    #     return mask

    def broadcast_ip(self):
        broadcast = list()
        mask = [entreeMasque5.get(), entreeMasque6.get(), entreeMasque7.get(), entreeMasque8.get()]
        self.binary_Mask = _dec_to_binary(mask)
        self.negation_Mask = _dec_to_binary(_negation_mask(mask))
        for x, y in zip(self.binary_IP, self.negation_Mask):
            broadcast.append(int(x, 2) | int(y, 2))
        self.broadcast = broadcast
        entreeBC1.delete(0,END)
        entreeBC2.delete(0,END)
        entreeBC3.delete(0,END)
        entreeBC4.delete(0,END)
        entreeBC1.insert(0,broadcast[0])
        entreeBC2.insert(0,broadcast[1])
        entreeBC3.insert(0,broadcast[2])
        entreeBC4.insert(0,broadcast[3])
   

        return broadcast



def ip_calculate(ip1,ip2,ip3,ip4):
    ip_address = str(ip1)+ "." +str(ip2) + "." + str(ip3) + "." + str(ip4)
    ip = IPCalculator(ip_address)
    ip.__repr__()

def choixBR():		# Fonction associée au boutons radio
    print('Boutons radio : ',str(svRadio.get()))
    ConversionPage1()

def choixBR2():		# Fonction associée au boutons radio page 2
    print('Boutons radio : ',str(svRadio2.get()))
    ConversionPage2()

def AppelPage1():
    ConversionPage1()

def AppelPage2():
    ConversionPage2()

def ConversionPage1() :
    BoutonChoix = int(svRadio.get())
    try :
        IP1 = int(entreeIP1.get())
    except:
        fenetreA = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreA.title('Erreur')
        fenetreA.geometry('400x100+300+500')
        LegendeErreur1 = Label(fenetreA, text='Erreur, votre Premiere entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try :
        IP2 = int(entreeIP2.get())
    except:
        fenetreB = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreB.title('Erreur')
        fenetreB.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreB, text='Erreur, votre Deuxieme entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try : 
        IP3 = int(entreeIP3.get())
    except:
        fenetreC = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreC.title('Erreur')
        fenetreC.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreC, text='Erreur, votre Troisieme entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50) 
    try :
        IP4 = int(entreeIP4.get())
    except:
        fenetreE = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreE.title('Erreur')
        fenetreE.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreE, text='Erreur, votre Quatrieme entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try :
        CIDR = int(entreeCIDR.get())
    except:
        fenetreF = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreF.title('Erreur')
        fenetreF.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreF, text='Erreur, votre entrée de CIDR ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)

    if BoutonChoix == 1 :
            if IP1 <128 and IP1 >= 0 :
                ResultatClasse1.delete(0,END)
                ResultatClasse1.insert(0,"Classe A")
                entreeMasque1.delete(0,END)
                entreeMasque1.insert(0,255)
                entreeMasque2.delete(0,END)
                entreeMasque2.insert(0,0)
                entreeMasque3.delete(0,END)
                entreeMasque3.insert(0,0)
                entreeMasque4.delete(0,END)
                entreeMasque4.insert(0,0)
                entreeCIDR2.delete(0,END)
                entreeCIDR2.insert(0,"/8")
                entreeNSR1.delete(0,END)
                entreeMSR1.delete(0,END)
                entreeNSR1.insert(0,255)
                entreeMSR1.insert(0,16777214)
            elif IP1 <192 and IP1 >=128 :
                ResultatClasse1.delete(0,END)
                ResultatClasse1.insert(0,"Classe B")
                entreeMasque1.delete(0,END)
                entreeMasque1.insert(0,255)
                entreeMasque2.delete(0,END)
                entreeMasque2.insert(0,255)
                entreeMasque3.delete(0,END)
                entreeMasque3.insert(0,0)
                entreeMasque4.delete(0,END)
                entreeMasque4.insert(0,0)
                entreeCIDR2.delete(0,END)
                entreeCIDR2.insert(0,"/16")
                entreeNSR1.delete(0,END)
                entreeMSR1.delete(0,END)
                entreeNSR1.insert(0,255)
                entreeMSR1.insert(0,65534)
            elif IP1 <224 and IP1 >=192 :
                ResultatClasse1.delete(0,END)
                ResultatClasse1.insert(0,"Classe C")
                entreeMasque1.delete(0,END)
                entreeMasque1.insert(0,255)
                entreeMasque2.delete(0,END)
                entreeMasque2.insert(0,255)
                entreeMasque3.delete(0,END)
                entreeMasque3.insert(0,255)
                entreeMasque4.delete(0,END)
                entreeMasque4.insert(0,0)
                entreeCIDR2.delete(0,END)
                entreeCIDR2.insert(0,"/24")
                entreeNSR1.delete(0,END)
                entreeMSR1.delete(0,END)
                entreeNSR1.insert(0,255)
                entreeMSR1.insert(0,254)
            elif IP1 <240 and IP1 >=224 :
                ResultatClasse1.delete(0,END)
                ResultatClasse1.insert(0,"Classe D")
                entreeMasque1.delete(0,END)
                entreeMasque1.insert(0,255)
                entreeMasque2.delete(0,END)
                entreeMasque2.insert(0,255)
                entreeMasque3.delete(0,END)
                entreeMasque3.insert(0,255)
                entreeMasque4.delete(0,END)
                entreeMasque4.insert(0,255)
                entreeCIDR2.delete(0,END)
                entreeCIDR2.insert(0,"/32")
                entreeNSR1.delete(0,END)
                entreeMSR1.delete(0,END)
                entreeNSR1.insert(0,1)
                entreeMSR1.insert(0,1)
            elif IP1 <248 and IP1 >=240 :
                ResultatClasse1.delete(0,END)
                ResultatClasse1.insert(0,"Classe E")
                entreeMasque1.delete(0,END)
                entreeMasque1.insert(0,255)
                entreeMasque2.delete(0,END)
                entreeMasque2.insert(0,255)
                entreeMasque3.delete(0,END)
                entreeMasque3.insert(0,255)
                entreeMasque4.delete(0,END)
                entreeMasque4.insert(0,255)
                entreeCIDR2.delete(0,END)
                entreeCIDR2.insert(0,"/32")
                entreeNSR1.delete(0,END)
                entreeMSR1.delete(0,END)
                entreeNSR1.insert(0,1)
                entreeMSR1.insert(0,1)
    elif BoutonChoix == 2 :
        ResultatClasse1.delete(0,END)
        ResultatClasse1.insert(0,"Classe A")
        entreeMasque1.delete(0,END)
        entreeMasque1.insert(0,255)
        entreeMasque2.delete(0,END)
        entreeMasque2.insert(0,0)
        entreeMasque3.delete(0,END)
        entreeMasque3.insert(0,0)
        entreeMasque4.delete(0,END)
        entreeMasque4.insert(0,0)
        entreeCIDR2.delete(0,END)
        entreeCIDR2.insert(0,"/8")
        entreeNSR1.delete(0,END)
        entreeMSR1.delete(0,END)
        entreeNSR1.insert(0,255)
        entreeMSR1.insert(0,16777214)
    elif BoutonChoix == 3 :
        ResultatClasse1.delete(0,END)
        ResultatClasse1.insert(0,"Classe B")
        entreeMasque1.delete(0,END)
        entreeMasque1.insert(0,255)
        entreeMasque2.delete(0,END)
        entreeMasque2.insert(0,255)
        entreeMasque3.delete(0,END)
        entreeMasque3.insert(0,0)
        entreeMasque4.delete(0,END)
        entreeMasque4.insert(0,0)
        entreeCIDR2.delete(0,END)
        entreeCIDR2.insert(0,"/16")
        entreeNSR1.delete(0,END)
        entreeMSR1.delete(0,END)
        entreeNSR1.insert(0,255)
        entreeMSR1.insert(0,65534)
    elif BoutonChoix == 4 :
        ResultatClasse1.delete(0,END)
        ResultatClasse1.insert(0,"Classe C")
        entreeMasque1.delete(0,END)
        entreeMasque1.insert(0,255)
        entreeMasque2.delete(0,END)
        entreeMasque2.insert(0,255)
        entreeMasque3.delete(0,END)
        entreeMasque3.insert(0,255)
        entreeMasque4.delete(0,END)
        entreeMasque4.insert(0,0)
        entreeCIDR2.delete(0,END)
        entreeCIDR2.insert(0,"/24")
        entreeNSR1.delete(0,END)
        entreeMSR1.delete(0,END)
        entreeNSR1.insert(0,255)
        entreeMSR1.insert(0,254)
    elif BoutonChoix == 5 :
        print(CIDR)
        if CIDR == 0 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,0)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/0")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,0)
            entreeMSR1.insert(0,4294967294)
        elif CIDR == 1 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,128)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/1")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,2)
            entreeMSR1.insert(0,2147483646)
        elif CIDR == 2 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,192)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/2")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,4)
            entreeMSR1.insert(0,1073741822)
        elif CIDR == 3 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,224)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/3")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,8)
            entreeMSR1.insert(0,536870910)
        elif CIDR == 4 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,240)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/4")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,16)
            entreeMSR1.insert(0,268435454)
        elif CIDR == 5 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,248)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,32)
            entreeMSR1.insert(0,134217726)
        elif CIDR == 6 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,252)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/6")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,64)
            entreeMSR1.insert(0,67108862)
        elif CIDR == 7 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,254)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/7")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,128)
            entreeMSR1.insert(0,33554430)
        elif CIDR == 8 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe A")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,0)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/8")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,255)
            entreeMSR1.insert(0,16777214)
        elif CIDR == 9 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,128)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/9")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,2)
            entreeMSR1.insert(0,8388606)
        elif CIDR == 10 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,192)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/10")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,4)
            entreeMSR1.insert(0,4194302)

        elif CIDR == 11 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,224)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/11")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,8)
            entreeMSR1.insert(0,2097150)

        elif CIDR == 12 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,240)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/12")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,16)
            entreeMSR1.insert(0,1048574)

        elif CIDR == 13 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,248)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/13")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,32)
            entreeMSR1.insert(0,524286)

        elif CIDR == 14 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,252)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/14")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,64)
            entreeMSR1.insert(0,262142)

        elif CIDR == 15 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,254)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/15")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,128)
            entreeMSR1.insert(0,262142)

        elif CIDR == 16 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe B")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,0)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/16")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,255)
            entreeMSR1.insert(0,65534)

        elif CIDR == 17 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,128)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/17")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,2)
            entreeMSR1.insert(0,32766)

        elif CIDR == 18 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,192)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/18")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,4)
            entreeMSR1.insert(0,16382)

        elif CIDR == 19 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,224)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/19")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,8)
            entreeMSR1.insert(0,8190)

        elif CIDR == 20 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,240)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/20")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,16)
            entreeMSR1.insert(0,4094)

        elif CIDR == 21 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,248)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/21")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,32)
            entreeMSR1.insert(0,2046)

        elif CIDR == 22 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,252)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/22")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,64)
            entreeMSR1.insert(0,1022)

        elif CIDR == 23 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,254)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/23")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,128)
            entreeMSR1.insert(0,510)

        elif CIDR == 24 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe C")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/24")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,255)
            entreeMSR1.insert(0,254)

        elif CIDR == 25 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,128)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/25")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,2)
            entreeMSR1.insert(0,126)


        elif CIDR == 26 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,192)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/26")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,4)
            entreeMSR1.insert(0,62)

        elif CIDR == 27 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,224)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/27")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,8)
            entreeMSR1.insert(0,30)

        elif CIDR == 28 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,240)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/28")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,16)
            entreeMSR1.insert(0,14)

        elif CIDR == 29 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,248)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/29")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,32)
            entreeMSR1.insert(0,6)

        elif CIDR == 30 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,252)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/30")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,64)
            entreeMSR1.insert(0,2)


        elif CIDR == 31 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,254)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/31")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,128)
            entreeMSR1.insert(0,2)

        elif CIDR == 32 :
            ResultatClasse1.delete(0,END)
            ResultatClasse1.insert(0,"Classe D")
            entreeMasque1.delete(0,END)
            entreeMasque1.insert(0,255)
            entreeMasque2.delete(0,END)
            entreeMasque2.insert(0,255)
            entreeMasque3.delete(0,END)
            entreeMasque3.insert(0,255)
            entreeMasque4.delete(0,END)
            entreeMasque4.insert(0,255)
            entreeCIDR2.delete(0,END)
            entreeCIDR2.insert(0,"/32")
            entreeNSR1.delete(0,END)
            entreeMSR1.delete(0,END)
            entreeNSR1.insert(0,255)
            entreeMSR1.insert(0,1)

def ConversionPage2() :
    BoutonChoix = int(svRadio2.get())
    try :
        IP1 = int(entreeIP5.get())
    except:
        fenetreA = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreA.title('Erreur')
        fenetreA.geometry('400x100+300+500')
        LegendeErreur1 = Label(fenetreA, text='Erreur, votre Premiere entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try :
        IP2 = int(entreeIP6.get())
    except:
        fenetreB = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreB.title('Erreur')
        fenetreB.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreB, text='Erreur, votre Deuxieme entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try : 
        IP3 = int(entreeIP7.get())
    except:
        fenetreC = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreC.title('Erreur')
        fenetreC.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreC, text='Erreur, votre Troisieme entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50) 
    try :
        IP4 = int(entreeIP8.get())
    except:
        fenetreE = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreE.title('Erreur')
        fenetreE.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreE, text='Erreur, votre Quatrieme entrée ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try :
        Masque1 = int(entreeMasque5.get())
    except:
        fenetreA = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreA.title('Erreur')
        fenetreA.geometry('400x100+300+500')
        LegendeErreur1 = Label(fenetreA, text='Erreur, votre Premiere entrée du masque ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try :
        Masque2 = int(entreeMasque6.get())
    except:
        fenetreB = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreB.title('Erreur')
        fenetreB.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreB, text='Erreur, votre Deuxieme entrée du masque ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    try : 
        Masque3 = int(entreeMasque7.get())
    except:
        fenetreC = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreC.title('Erreur')
        fenetreC.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreC, text='Erreur, votre Troisieme entrée du masque ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50) 
    try :
        Masque4 = int(entreeMasque8.get())
    except:
        fenetreE = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
        fenetreE.title('Erreur')
        fenetreE.geometry('300x100+300+500')
        LegendeErreur1 = Label(fenetreE, text='Erreur, votre Quatrieme entrée du masque ne correspond pas a un nombre !!!')
        LegendeErreur1.place(x=0, y=50)
    
    if BoutonChoix == 1 :
        entreeIP9.delete(0,END)
        entreeIP10.delete(0,END)
        entreeIP11.delete(0,END)
        entreeIP12.delete(0,END)
        

        ip_calculate(IP1, IP2, IP3, IP4)
        IP_reseau1 = IP1&Masque1
        IP_reseau2 = IP2&Masque2
        IP_reseau3 = IP3&Masque3
        IP_reseau4 = IP4&Masque4

        ip_address = str(IP_reseau1)+ "." +str(IP_reseau2) + "." + str(IP_reseau3) + "." + str(IP_reseau4)
        ip_mask = str(Masque1)+ "." +str(Masque2) + "." + str(Masque3) + "." + str(Masque4)
        ip = str(ip_address)+"/"+str(ip_mask)
        l1 = list(ip_network(ip).hosts())
        hosts = 0
        for i in l1 :
            hosts = hosts + 1
        print(hosts)

        CIDR = str(ip_network(ip))

        CIDR1 = str(CIDR).split('.')
        CIDR2 = str(CIDR1[3]).split('/')
        CIDR1 = CIDR2[1]
        print(CIDR1)
        CIDR1 = int(CIDR1)

        entreeNSR2.delete(0,END)
        
        if CIDR1 == 0 :
            entreeNSR2.insert(0,1)
        elif CIDR1 == 1 :
            entreeNSR2.insert(0,2)
        elif CIDR1 == 2 :
            entreeNSR2.insert(0,4)
        elif CIDR1 == 3 :
            entreeNSR2.insert(0,8)
        elif CIDR1 == 4 :
            entreeNSR2.insert(0,16)
        elif CIDR1 == 5 :
            entreeNSR2.insert(0,32)
        elif CIDR1 == 6 :
            entreeNSR2.insert(0,64)
        elif CIDR1 == 7 :
            entreeNSR2.insert(0,128)
        elif CIDR1 == 8 :
            entreeNSR2.insert(0,255)
        elif CIDR1 == 9 :
            entreeNSR2.insert(0,2)
        elif CIDR1 == 10 :
            entreeNSR2.insert(0,4)
        elif CIDR1 == 11 :
            entreeNSR2.insert(0,8)
        elif CIDR1 == 12 :
            entreeNSR2.insert(0,16)
        elif CIDR1 == 13 :
            entreeNSR2.insert(0,32)
        elif CIDR1 == 14 :
            entreeNSR2.insert(0,64)
        elif CIDR1 == 15 :
            entreeNSR2.insert(0,128)
        elif CIDR1 == 16 :
            entreeNSR2.insert(0,255)
        elif CIDR1 == 17 :
            entreeNSR2.insert(0,2)
        elif CIDR1 == 18 :
            entreeNSR2.insert(0,4)
        elif CIDR1 == 19 :
            entreeNSR2.insert(0,8)
        elif CIDR1 == 20 :
            entreeNSR2.insert(0,16)
        elif CIDR1 == 21 :
            entreeNSR2.insert(0,32)
        elif CIDR1 == 22 :
            entreeNSR2.insert(0,64)
        elif CIDR1 == 23 :
            entreeNSR2.insert(0,128)
        elif CIDR1 == 24 :
            entreeNSR2.insert(0,255)
        elif CIDR1 == 25 :
            entreeNSR2.insert(0,2)
        elif CIDR1 == 26 :
            entreeNSR2.insert(0,4)
        elif CIDR1 == 27 :
            entreeNSR2.insert(0,8)
        elif CIDR1 == 28 :
            entreeNSR2.insert(0,16)
        elif CIDR1 == 29 :
            entreeNSR2.insert(0,32)
        elif CIDR1 == 30 :
            entreeNSR2.insert(0,64)
        elif CIDR1 == 31 :
            entreeNSR2.insert(0,128)
        elif CIDR1 == 32 :
            entreeNSR2.insert(0,255)

        if  IP1 & Masque1 != 0 :
            entreeIP9.insert(0,IP_reseau1)    
        else :
            entreeIP9.insert(0,IP_reseau1)

        if  IP2 & Masque2 != 0 :
            entreeIP10.insert(0,IP_reseau2)
        else :
            entreeIP10.insert(0,IP_reseau2)

        if IP3 & Masque3 != 0 :
            entreeIP11.insert(0,IP_reseau3)
        else :
            entreeIP11.insert(0,IP_reseau3)

        if IP4 & Masque4 != 0 :
            entreeIP12.insert(0,IP_reseau4)
        else :
            entreeIP12.insert(0,IP_reseau4)  
        entreeMSR2.delete(0,END)
        entreeMSR2.insert(0,hosts)


    elif BoutonChoix == 2 :
        IP_reseau1 = IP1&Masque1
        IP_reseau2 = IP2&Masque2
        IP_reseau3 = IP3&Masque3
        IP_reseau4 = IP4&Masque4

        ip_address = str(IP_reseau1) + "." + str(IP_reseau2) + "." + str(IP_reseau3) + "." + str(IP_reseau4)
        ip = str(ip_address) + "/" + "255.0.0.0"
        l1 = list(ip_network(ip).hosts())

        hosts = 0
        for i in l1 :
            hosts = hosts + 1
        print(hosts)


        entreeIP9.delete(0,END)
        entreeIP9.insert(0,IP1 & 255)
        entreeIP10.delete(0,END)
        entreeIP10.insert(0,0)
        entreeIP11.delete(0,END)
        entreeIP11.insert(0,0)
        entreeIP12.delete(0,END)
        entreeIP12.insert(0,0)
        entreeBC1.delete(0,END)
        entreeBC1.insert(0, IP1 & 255)
        entreeBC2.delete(0,END)
        entreeBC2.insert(0,255)
        entreeBC3.delete(0,END)
        entreeBC3.insert(0,255)
        entreeBC4.delete(0,END)
        entreeBC4.insert(0,255)
        entreeNSR2.delete(0,END)
        entreeNSR2.insert(0,1)
        entreeMSR2.delete(0,END)
        entreeMSR2.insert(0,(2**24)-2)



    elif BoutonChoix == 3 :

        IP_reseau1 = IP1&Masque1
        IP_reseau2 = IP2&Masque2
        IP_reseau3 = IP3&Masque3
        IP_reseau4 = IP4&Masque4

        ip_address = str(IP_reseau1) + "." + str(IP_reseau2) + "." + str(IP_reseau3) + "." + str(IP_reseau4)
        ip = str(ip_address) + "/" + "255.255.0.0"
        l1 = list(ip_network(ip).hosts())

        hosts = 0
        for i in l1 :
            hosts = hosts + 1
        print(hosts)

        entreeIP9.delete(0,END)
        entreeIP9.insert(0,IP1 & 255)
        entreeIP10.delete(0,END)
        entreeIP10.insert(0,IP2 & 255)
        entreeIP11.delete(0,END)
        entreeIP11.insert(0,0)
        entreeIP12.delete(0,END)
        entreeIP12.insert(0,0)
        entreeBC1.delete(0,END)
        entreeBC1.insert(0,IP1 & 255)
        entreeBC2.delete(0,END)
        entreeBC2.insert(0,IP2 & 255)
        entreeBC3.delete(0,END)
        entreeBC3.insert(0,255)
        entreeBC4.delete(0,END)
        entreeBC4.insert(0,255)
        entreeNSR2.delete(0,END)
        entreeNSR2.insert(0,1)
        entreeMSR2.delete(0,END)
        entreeMSR2.insert(0,(2**16)-2)



    elif BoutonChoix == 4 :
        
        IP_reseau1 = IP1&Masque1
        IP_reseau2 = IP2&Masque2
        IP_reseau3 = IP3&Masque3
        IP_reseau4 = IP4&Masque4

        ip_address = str(IP_reseau1) + "." + str(IP_reseau2) + "." + str(IP_reseau3) + "." + str(IP_reseau4)
        ip = str(ip_address) + "/" + "255.255.255.0"
        l1 = list(ip_network(ip).hosts())

        hosts = 0
        for i in l1 :
            hosts = hosts + 1
        print(hosts)

        entreeIP9.delete(0,END)
        entreeIP9.insert(0,IP1 & 255)
        entreeIP10.delete(0,END)
        entreeIP10.insert(0,IP2 & 255)
        entreeIP11.delete(0,END)
        entreeIP11.insert(0,IP3 & 255)
        entreeIP12.delete(0,END)
        entreeIP12.insert(0,0)
        entreeBC1.delete(0,END)
        entreeBC1.insert(0,IP1 & 255)
        entreeBC2.delete(0,END)
        entreeBC2.insert(0,IP2 & 255)
        entreeBC3.delete(0,END)
        entreeBC3.insert(0,IP3 & 255)
        entreeBC4.delete(0,END)
        entreeBC4.insert(0,255)
        entreeNSR2.delete(0,END)
        entreeNSR2.insert(0,1)
        entreeMSR2.delete(0,END)
        entreeMSR2.insert(0,(2**8)-2)


    elif BoutonChoix == 5 :
        try :
            CIDR1 = int(entreeCIDR3.get())
        except:
            fenetreF = Toplevel()	# Fenêtre auxiliaire -> Toplevel()
            fenetreF.title('Erreur')
            fenetreF.geometry('300x100+300+500')
            LegendeErreur1 = Label(fenetreF, text='Erreur, votre entrée de CIDR ne correspond pas a un nombre !!!')
            LegendeErreur1.place(x=0, y=50)
        print(CIDR1)

        
        entreeNSR2.delete(0, END)

        if CIDR1 == 0 :
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,1)
            entreeMSR2.insert(0,4294967294)
        elif CIDR1 == 1 :
            Masque1 = 128
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 128)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,2)
            entreeMSR2.insert(0,2147483646)
        elif CIDR1 == 2 :
            Masque1 = 192
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 192)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,4)
            entreeMSR2.insert(0,1073741822)
        elif CIDR1 == 3 :
            Masque1 = 224
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 224)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,8)
            entreeMSR2.insert(0,536870910)
        elif CIDR1 == 4 :
            Masque1 = 240
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 240)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,16)
            entreeMSR2.insert(0,268435454)
        elif CIDR1 == 5 :
            Masque1 = 248
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 248)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeCIDR2.delete(0,END)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,32)
            entreeMSR2.insert(0,134217726)
        elif CIDR1 == 6 :
            Masque1 = 252
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 252)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,64)
            entreeMSR2.insert(0,67108862)
        elif CIDR1 == 7 :
            Masque1 = 254
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 254)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,128)
            entreeMSR2.insert(0,33554430)
        elif CIDR1 == 8 :
            Masque1 = 255
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,0)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,255)
            entreeMSR2.insert(0,16777214)
        elif CIDR1 == 9 :
            Masque1 = 255
            Masque2 = 128
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 128)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,2)
            entreeMSR2.insert(0,8388606)
        elif CIDR1 == 10 :
            Masque1 = 255
            Masque2 = 192
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 192)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,4)
            entreeMSR2.insert(0,4194302)

        elif CIDR1 == 11 :
            Masque1 = 255
            Masque2 = 224
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 224)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,8)
            entreeMSR2.insert(0,2097150)

        elif CIDR1 == 12 :
            Masque1 = 255
            Masque2 = 240
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 240)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,16)
            entreeMSR2.insert(0,1048574)

        elif CIDR1 == 13 :
            Masque1 = 255
            Masque2 = 248
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 248)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,32)
            entreeMSR2.insert(0,524286)

        elif CIDR1 == 14 :
            Masque1 = 255
            Masque2 = 252
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 252)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,64)
            entreeMSR2.insert(0,262142)

        elif CIDR1 == 15 :
            Masque1 = 255
            Masque2 = 254
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 254)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,128)
            entreeMSR2.insert(0,262142)

        elif CIDR1 == 16 :
            Masque1 = 255
            Masque2 = 255
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,0)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,255)
            entreeMSR2.insert(0,65534)

        elif CIDR1 == 17 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 128
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 128)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,2)
            entreeMSR2.insert(0,32766)

        elif CIDR1 == 18 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 192
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 192)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,4)
            entreeMSR2.insert(0,16382)

        elif CIDR1 == 19 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 224
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 224)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,8)
            entreeMSR2.insert(0,8190)

        elif CIDR1 == 20 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 240
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 240)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,16)
            entreeMSR2.insert(0,4094)

        elif CIDR1 == 21 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 248
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 248)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,32)
            entreeMSR2.insert(0,2046)

        elif CIDR1 == 22 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 252
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 252)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,64)
            entreeMSR2.insert(0,1022)

        elif CIDR1 == 23 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 254
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 254)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,128)
            entreeMSR2.insert(0,510)

        elif CIDR1 == 24 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,0)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,255)
            entreeMSR2.insert(0,254)

        elif CIDR1 == 25 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 128
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 128)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,2)
            entreeMSR2.insert(0,126)


        elif CIDR1 == 26 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 192
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 192)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,4)
            entreeMSR2.insert(0,62)

        elif CIDR1 == 27 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 224
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 224)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,8)
            entreeMSR2.insert(0,30)

        elif CIDR1 == 28 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 240
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 240)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,16)
            entreeMSR2.insert(0,14)

        elif CIDR1 == 29 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 248
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 248)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,32)
            entreeMSR2.insert(0,6)

        elif CIDR1 == 30 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 252
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 252)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,64)
            entreeMSR2.insert(0,2)


        elif CIDR1 == 31 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 254
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 254)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,128)
            entreeMSR2.insert(0,2)

        elif CIDR1 == 32 :
            Masque1 = 255
            Masque2 = 255
            Masque3 = 255
            Masque4 = 255
            entreeIP9.delete(0,END)
            entreeIP9.insert(0,IP1 & 255)
            entreeIP10.delete(0,END)
            entreeIP10.insert(0,IP2 & 255)
            entreeIP11.delete(0,END)
            entreeIP11.insert(0,IP3 & 255)
            entreeIP12.delete(0,END)
            entreeIP12.insert(0,IP4 & 255)
            entreeNSR2.delete(0,END)
            entreeMSR2.delete(0,END)
            entreeNSR2.insert(0,255)
            entreeMSR2.insert(0,1)
        
        IP_reseau1 = IP1&Masque1
        IP_reseau2 = IP2&Masque2
        IP_reseau3 = IP3&Masque3
        IP_reseau4 = IP4&Masque4

        ip_address = str(IP_reseau1)+ "." +str(IP_reseau2) + "." + str(IP_reseau3) + "." + str(IP_reseau4)
        ip = str(ip_address)+"/"+str(CIDR1)

        print(ip)
        

        l1 = list(ip_network(ip).hosts())
        hosts = 0
        for i in l1 :
            hosts = hosts + 1
        print(hosts)

        bc = IPv4Network(ip).broadcast_address
        print(bc)

        bc2 = str(bc).split(".")
        print(bc2)

        entreeBC1.delete(0, END)
        entreeBC2.delete(0, END)
        entreeBC3.delete(0, END)
        entreeBC4.delete(0, END)
        entreeBC1.insert(0, bc2[0])
        entreeBC2.insert(0, bc2[1])
        entreeBC3.insert(0, bc2[2])
        entreeBC4.insert(0, bc2[3])

        # entreeNMSR.delete(0, END)


        




LegendeAdresse1 = Label(f1, text='Entrer un adresse IP  : ')
LegendeAdresse1.place(x=0, y=15)
entreeIP1 = Entry(f1)
entreeIP1.place(width=30, height=25, x=290, y=12)
entreeIP1.insert(0,191) 
entreeIP2 = Entry(f1)
entreeIP2.place(width=30, height=25, x=330, y=12)
entreeIP2.insert(0,1)
entreeIP3 = Entry(f1)
entreeIP3.place(width=30, height=25, x=370, y=12)
entreeIP3.insert(0,1)
entreeIP4 = Entry(f1)
entreeIP4.place(width=30, height=25, x=410, y=12)
entreeIP4.insert(0,1)


LegendeClasse1 = Label(f1, text='Forcer la classe  : ')
LegendeClasse1.place(x=0, y=55)
svRadio = IntVar()		
svRadio.set('1')
ClasseDefault1 = Radiobutton(f1, text='Défaut', variable=svRadio, value='1', command=choixBR).place(x=179, y=55)
ClasseA1 = Radiobutton(f1, text='Classe A', variable=svRadio, value='2', command=choixBR).place(x=240, y=55)
ClasseB1 = Radiobutton(f1, text='Classe B', variable=svRadio, value='3', command=choixBR).place(x=310, y=55)
ClasseC1 = Radiobutton(f1, text='Classe C', variable=svRadio, value='4', command=choixBR).place(x=379, y=55)

LegendeClasse1 = Label(f1, text='Forcer la classe  : ')
LegendeClasse1.place(x=0, y=55)

boutonquitter1 = Button(f1, text='Quitter', command=root.destroy).place(x=350, y=445)
boutonquitter2 = Button(f2, text='Quitter', command=root.destroy).place(x=350, y=445)
boutonquitter3 = Button(f3, text='Quitter', command=root.destroy).place(x=350, y=445)

LegendeCIDR1 = Label(f1, text='Ou sélectionner un CIDR  : ')
LegendeCIDR1.place(x=0, y=99)
boutonCIDR1 = Radiobutton(f1, text='CIDR', variable=svRadio, value='5', command=choixBR).place(x=310, y=99)
entreeCIDR = Entry(f1)
entreeCIDR.place(width=30, height=24, x=370, y=99)
entreeCIDR.insert(0,1)

# entreeSousReseau1 = tk.StringVar()
# entreeMachine1 = tk.StringVar()


# LegendeSR1 = Label(f1, text='Entrer le nombre de sous-réseaux requis  : ').place(x=0, y=141)
# cbSR1 = ttk.Combobox(f1,textvariable=entreeSousReseau1, values=["1","2","4","8","16","32","64","128"]).place(x=300,y=141)
# LegendeOU1 = Label(f1, text='Ou').place(x=20, y=161)
# LegendeM1 = Label(f1, text='Entrer le nombre de machine requise par sous-réseaux : ').place(x=0, y=181)
# cbM1 = ttk.Combobox(f1, textvariable=entreeMachine1, values=["1","2","6","14","30","62","126"]).place(x=300,y=181)




LegendeResultat1 = Label(f1, text='Resultat').place(x=0, y=180)

LegendeResultatClasse1 = Label(f1, text='Classe IP :').place(x=0, y=241)
ResultatClasse1 = Entry(f1)
ResultatClasse1.place(width=70, height=22, x=200, y=239)
# LegendeResultatClasse2 = Label(f1, text='en tant que :').place(x=270, y=241)
# ResultatClasse2 = Entry(f1)
# ResultatClasse2.place(width=70, height=22, x=340, y=239)

LegendeResultatMasque1 = Label(f1, text='Masque du Sous-réseau :').place(x=0, y=285)
entreeMasque1 = Entry(f1)
entreeMasque1.place(width=30, height=25, x=200, y=281)
entreeMasque2 = Entry(f1)
entreeMasque2.place(width=30, height=25, x=235, y=281)
entreeMasque3 = Entry(f1)
entreeMasque3.place(width=30, height=25, x=270, y=281)
entreeMasque4 = Entry(f1)
entreeMasque4.place(width=30, height=25, x=305, y=281)
LegendeOU2 = Label(f1, text='Ou').place(x=340, y=285)
entreeCIDR2 = Entry(f1)
entreeCIDR2.place(width=35, height=25, x=370, y=281)
entreeCIDR2.insert(0,"")

LegendeResultatNSR1 = Label(f1, text='Nombre de Sous-réseau :').place(x=0, y=330)
entreeNSR1 = Entry(f1)
entreeNSR1.place(width=210, height=25, x=200, y=327)

LegendeResultatMSR1 = Label(f1, text='Machine par Sous-réseau :').place(x=0, y=375)
entreeMSR1 = Entry(f1)
entreeMSR1.place(width=210, height=25, x=200, y=372)

BoutonConv = Button(f1, text='Convertir', command=AppelPage1).place(x=50, y=445)


LegendeAdresse2 = Label(f2, text='Entrer un adresse IP  : ')
LegendeAdresse2.place(x=0, y=15)
entreeIP5 = Entry(f2)
entreeIP5.place(width=30, height=25, x=290, y=12)
entreeIP5.insert(0,1)
entreeIP6 = Entry(f2)
entreeIP6.place(width=30, height=25, x=330, y=12)
entreeIP6.insert(0,1)
entreeIP7 = Entry(f2)
entreeIP7.place(width=30, height=25, x=370, y=12)
entreeIP7.insert(0,1)
entreeIP8 = Entry(f2)
entreeIP8.place(width=30, height=25, x=410, y=12)
entreeIP8.insert(0,1)

LegendeResultatMasque2 = Label(f2, text='Masque du Sous-réseau :').place(x=0, y=45)
entreeMasque5 = Entry(f2)
entreeMasque5.place(width=30, height=25, x=290, y=45)
entreeMasque5.insert(0,0)
entreeMasque6 = Entry(f2)
entreeMasque6.place(width=30, height=25, x=330, y=45)
entreeMasque6.insert(0,0)
entreeMasque7 = Entry(f2)
entreeMasque7.place(width=30, height=25, x=370, y=45)
entreeMasque7.insert(0,0)
entreeMasque8 = Entry(f2)
entreeMasque8.place(width=30, height=25, x=410, y=45)
entreeMasque8.insert(0,0)

LegendeClasse2 = Label(f2, text='Forcer la classe  : ')
LegendeClasse2.place(x=0, y=75)
svRadio2 = StringVar()		
svRadio2.set('1')
ClasseDefault2 = Radiobutton(f2, text='Défaut', variable=svRadio2, value='1', command=choixBR2).place(x=179, y=75)
ClasseA2 = Radiobutton(f2, text='Classe A', variable=svRadio2, value='2', command=choixBR2).place(x=240, y=75)
ClasseB2 = Radiobutton(f2, text='Classe B', variable=svRadio2, value='3', command=choixBR2).place(x=310, y=75)
ClasseC2 = Radiobutton(f2, text='Classe C', variable=svRadio2, value='4', command=choixBR2).place(x=379, y=75)

LegendeCIDR3 = Label(f2, text='Ou sélectionner un CIDR  : ')
LegendeCIDR3.place(x=0, y=105)
boutonCIDR4 = Radiobutton(f2, text='CIDR', variable=svRadio2, value='5', command=choixBR2).place(x=310, y=105)
entreeCIDR3 = Entry(f2)
entreeCIDR3.place(width=30, height=24, x=370, y=105)
entreeCIDR3.insert(0,0)

BoutonConv2 = Button(f2, text='Convertir', command=AppelPage2).place(x=50, y=445)

LegendeResultat1 = Label(f2, text='Resultat').place(x=0, y=181)

LegendeAdresse3 = Label(f2, text='Adresse de Sous-réseau : ')
LegendeAdresse3.place(x=0, y=205)
entreeIP9 = Entry(f2)
entreeIP9.place(width=30, height=25, x=290, y=205)
entreeIP9.insert(0,0)
entreeIP10 = Entry(f2)
entreeIP10.place(width=30, height=25, x=330, y=205)
entreeIP10.insert(0,0) 
entreeIP11 = Entry(f2)
entreeIP11.place(width=30, height=25, x=370, y=205)
entreeIP11.insert(0,0)
entreeIP12 = Entry(f2)
entreeIP12.place(width=30, height=25, x=410, y=205)
entreeIP12.insert(0,0)

LegendeBC1 = Label(f2, text='Adresse de Broadcast : ')
LegendeBC1.place(x=0, y=230)
entreeBC1 = Entry(f2)
entreeBC1.place(width=30, height=25, x=290, y=230)
entreeBC1.insert(0,0)
entreeBC2 = Entry(f2)
entreeBC2.place(width=30, height=25, x=330, y=230)
entreeBC2.insert(0,0)
entreeBC3 = Entry(f2)
entreeBC3.place(width=30, height=25, x=370, y=230)
entreeBC3.insert(0,0)
entreeBC4 = Entry(f2)
entreeBC4.place(width=30, height=25, x=410, y=230)
entreeBC4.insert(0,0)

LegendeResultatNSR2 = Label(f2, text='Nombre de Sous-réseau :').place(x=0, y=260)
entreeNSR2 = Entry(f2)
entreeNSR2.place(width=150, height=25, x=290, y=260)
entreeNSR2.insert(0,0)


LegendeResultatMSR2 = Label(f2, text='Machine par Sous-réseau :').place(x=0, y=290)
entreeMSR2 = Entry(f2)
entreeMSR2.place(width=150, height=25, x=290, y=290)
entreeMSR2.insert(0,0)


# LegendeResultatNMSR = Label(f2, text='Numero de Machine dans ce Sous-réseau :').place(x=0, y=320)
# entreeNMSR = Entry(f2)
# entreeNMSR.place(width=150, height=25, x=290, y=320)
# entreeNMSR.insert(0,0)

# Page 3

LegendeAdresse3 = Label(f3, text='Notation Decimale')
LegendeAdresse3.place(x=0, y=15)
entreeIP13 = Entry(f3)
entreeIP13.place(width=30, height=25, x=290, y=12)
entreeIP14 = Entry(f3)
entreeIP14.place(width=30, height=25, x=330, y=12)
entreeIP15 = Entry(f3)
entreeIP15.place(width=30, height=25, x=370, y=12)
entreeIP16 = Entry(f3)
entreeIP16.place(width=30, height=25, x=410, y=12)

LegendeResultatNB1 = Label(f3, text='Notation Hexadecimale').place(x=0, y=40)
entreeNHexa = Entry(f3)
entreeNHexa.place(width=150, height=25, x=290, y=40)

LegendeBinaire = Label(f3, text='Notation Binaire')
LegendeBinaire.place(x=0, y=75)
entreeIP13 = Entry(f3)
entreeIP13.place(width=60, height=25, x=200, y=75)
entreeIP14 = Entry(f3)
entreeIP14.place(width=60, height=25, x=260, y=75)
entreeIP15 = Entry(f3)
entreeIP15.place(width=60, height=25, x=320, y=75)
entreeIP16 = Entry(f3)
entreeIP16.place(width=60, height=25, x=380, y=75)

LegendeConvSR1 = Label(f3, text='Convertisseur de Masque de Sous-réseaux').place(x=0, y=200)

LegendeMasque1 = Label(f3, text='Masque en notation decimale')
LegendeMasque1.place(x=0, y=250)
entreeMasque9 = Entry(f3)
entreeMasque9.place(width=30, height=25, x=290, y=250)
entreeMasque10 = Entry(f3)
entreeMasque10.place(width=30, height=25, x=330, y=250)
entreeMasque11 = Entry(f3)
entreeMasque11.place(width=30, height=25, x=370, y=250)
entreeMasque12 = Entry(f3)
entreeMasque12.place(width=30, height=25, x=410, y=250)


LegendeCIDR3 = Label(f3, text='Masque en notation CIDR ')
LegendeCIDR3.place(x=0, y=310)
entreeCIDR4 = Entry(f3)
entreeCIDR4.place(width=60, height=24, x=370, y=310)
               


root.mainloop()
