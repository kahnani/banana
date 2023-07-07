import tkinter as tk
from tkinter.filedialog import asksaveasfilename,askopenfilename
#testing again
class NewForm(tk.Toplevel):
    keys = ['Name','Price']
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.resizable(False,False)
        self.title('Add item')

        self.grab_set()

        self.labels={}
        self.variables={}

        for key in NewForm.keys:
            self.labels[key] = ''
            self.variables[key] = tk.StringVar()

        for label in self.labels.keys():
            frm = tk.Frame(self,relief=tk.RAISED,bd = 2)
            frm.pack(side=tk.TOP,expand=tk.YES,fill=tk.X)
            tk.Label(frm,text=label).pack(side=tk.LEFT)
            ent = tk.Entry(frm,textvar = self.variables[label])
            ent.pack(side=tk.RIGHT)

        tk.Button(self,text='Submit',command=self.Submit).pack(side=tk.TOP)

        self.wait_window()
    def Submit(self):
        for variable_value in self.variables.values():
            if len(variable_value.get())==0:
                tk.messagebox.showinfo('Warning','The fields are incomplete!')
                return
        self.destroy()

class Main(tk.Frame):

    def __init__(self,parent = None):
        tk.Frame.__init__(self,parent,relief = tk.RIDGE,bd=4,
                          width = 400,height = 300)
        self.master.title('Grocery List')
        self.pack(expand=tk.YES,fill=tk.BOTH)
        parent.minsize(width = 300,height=200)
        parent.maxsize(width = 500,height =400)

        self.add_menu()
        self.add_info()

        self.add_buttons()


    def add_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        file = tk.Menu(self.menu,tearoff=False)
        file.add_command(label='Open',command = self.file_open)
        file.add_command(label='Save',command = self.file_save)
        file.add_command(label='Save and Exit',command = self.file_save_exit)
        self.menu.add_cascade(label='File',menu = file)

    def add_info(self):
        info_frame = tk.Frame(self,relief=tk.SUNKEN,bd=2)
        info_frame.pack(side=tk.TOP,expand=tk.YES,fill=tk.BOTH)
        self.sbar = tk.Scrollbar(info_frame)
        self.lbox = tk.Listbox(info_frame,relief = tk.SUNKEN,selectmode='multiple')

        self.sbar.config(command = self.lbox.yview)
        self.lbox.config(yscrollcommand = self.sbar.set)

        self.sbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.lbox.pack(side=tk.TOP,expand = tk.YES,fill=tk.BOTH)

    def add_buttons(self):
        frame = tk.Frame(self,relief = tk.RAISED,bd=2)
        frame.pack(side=tk.TOP,expand=tk.YES,fill=tk.BOTH)
        tk.Button(frame,text='Add grocery item',
                        command = self.add_item).pack(side=tk.LEFT,
                                                         expand=tk.YES)                                                          
        tk.Button(frame,text='Delete grocery item',
                  command = self.delete_item).pack(side=tk.LEFT,
                                                   expand=tk.YES)
    def add_item(self):
        self.popup = NewForm()
        self.update_list()

    def delete_item(self):
        idx_to_delete = self.lbox.curselection()
        for idx in idx_to_delete[::-1]:
            self.lbox.delete(idx)

    def update_list(self):
        self.lbox.insert(0,self.popup.variables['Name'].get()+', '+self.popup.variables['Price'].get()+'\n')

    def file_open(self):
        file = askopenfilename()
        with open(file,'r') as f:
            contents = f.readlines()
            for line in contents:
                self.lbox.insert(0,line)

    def file_save(self):
        filename = asksaveasfilename()
        if filename:
            with open(filename,'w') as f:
                for line in self.lbox.get(0,tk.END):
                    f.write(line)

    def file_save_exit(self):
        self.file_save()
        self.master.destroy()

Main(tk.Tk()).mainloop()