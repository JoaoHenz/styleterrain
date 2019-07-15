from tkinter import *                # python 3
from tkinter import font  as tkfont # python 3
from PIL import ImageTk, Image
import os
import tools.create_heightmap as hm
import tools.add_water as wa
import tools.add_texture as te

options = [
    'Tropical and Subtropical Moist Broadleaf Forests',
    'Tropical and Subtropical Dry Broadleaf Forests',
    'Tropical and Subtropical Coniferous Forests',
    'Temperate Broadleaf and Mixed Forests',

    'Temperate Coniferous Forests',
    'Boreal Forests',
    'Tropical and Subtropical Grasslands, Savanas or Shrublands',
    'Temperate Grasslands, Savannas and Shrublands',

    'Flooded Grasslands and Savannas',
    'Montane Grasslands and Shrublands',
    'Tundra',
    'Mediterranean Forests, Woodlands and Scrub',

    'Deserts and Xeric Shrublands',
    'Lakes',
    'Rock and Ice',
    ]

biome_nicks = {
    'Tropical and Subtropical Moist Broadleaf Forests' : 'TSMBForest',
    'Tropical and Subtropical Dry Broadleaf Forests' : 'TSDBForest',
    'Tropical and Subtropical Coniferous Forests' : 'TSCForest',
    'Temperate Broadleaf and Mixed Forests' : 'PBMForest',

    'Temperate Coniferous Forests' : 'PCForest',
    'Boreal Forests' : 'BForest',
    'Tropical and Subtropical Grasslands, Savanas or Shrublands' : 'TSGrassland',
    'Temperate Grasslands, Savannas and Shrublands' : 'PGrassland',

    'Flooded Grasslands and Savannas' : 'FGrassland',
    'Montane Grasslands and Shrublands' : 'MGrassland',
    'Tundra' : 'Tundra',
    'Mediterranean Forests, Woodlands and Scrub' : 'DForest',

    'Deserts and Xeric Shrublands' : 'Desert',
    'Lakes' : 'Lake',
    'Rock and Ice' : 'RockIce',
}

def updateImages(frame):
    frame.img = ImageTk.PhotoImage(Image.open("output/heightmap.tif"))
    frame.canvas.itemconfig(frame.image_on_canvas, image = frame.img )

    frame.img2 = ImageTk.PhotoImage(Image.open("output/watermap.tif"))
    frame.canvas2.itemconfig(frame.image_on_canvas2, image = frame.img2 )

    frame.img3 = ImageTk.PhotoImage(Image.open("output/texturemap.tif"))
    frame.canvas3.itemconfig(frame.image_on_canvas3, image = frame.img3)

    frame.img4 = ImageTk.PhotoImage(Image.open("output/heightmap_initial.tif"))
    frame.canvas4.itemconfig(frame.image_on_canvas4, image = frame.img4 )

class SampleApp(Tk):

    def __init__(self, *args, **kwargs): #controller
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.fontePadrao = ("Arial", "10")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

        if page_name == 'PageOne' or page_name == 'PageTwo'or page_name == 'PageThree':
            updateImages(frame)

class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="StyleTerrain Tool", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.label1 = Label(self,text="Choose one of the options of how to generate terrains", font=controller.fontePadrao)
        self.label1.pack(pady=10)

        button1 = Button(self, text="Biomes Representations StyleMixing",
                            command=lambda: controller.show_frame("PageOne"),pady=10)
        button2 = Button(self, text="Biome Oriented Terrain Generation",
                            command=lambda: controller.show_frame("PageTwo"),pady=10)
        button3 = Button(self, text="Biome Oriented Terrain Generation with Seed Input",
                            command=lambda: controller.show_frame("PageThree"),pady=10)
        button1.pack()
        button2.pack()
        button3.pack()

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Biomes Representations StyleMixing", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.con1 = Frame(self)
        self.con1["padx"] = 10
        self.con1["pady"] = 10
        self.con1.pack()

        self.con_i = Frame(self)
        self.con_i["padx"] = 10
        self.con_i["pady"] = 10
        self.con_i.pack()

        self.con2 = Frame(self)
        self.con2["padx"] = 10
        self.con2["pady"] = 10
        self.con2.pack()

        self.con3 = Frame(self)
        self.con3["padx"] = 10
        self.con3["pady"] = 10
        self.con3.pack()

        self.con4 = Frame(self)
        self.con4["padx"] = 10
        self.con4["pady"] = 10
        self.con4.pack()

        self.conwater = Frame(self)
        self.conwater["padx"] = 10
        self.conwater["pady"] = 10
        self.conwater.pack()

        self.con5 = Frame(self)
        self.con5["padx"] = 10
        self.con5["pady"] = 10
        self.con5.pack()

        self.con_images = Frame(self)
        self.con_images["padx"] = 10
        self.con_images["pady"] = 10
        self.con_images.pack()

        # self.label1 = Label(self.con1,text="STYLETERRAIN TOOL", font=controller.fontePadrao)
        # self.label1.pack()

        self.canvas4 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas4.pack(side=LEFT)
        self.img4 = ImageTk.PhotoImage(Image.open("output/heightmap_initial.tif"))
        self.image_on_canvas4 = self.canvas4.create_image(20, 20, anchor=NW, image=self.img4)

        self.canvas = Canvas(self.con_images, width = 200, height = 200)
        self.canvas.pack(side=LEFT)
        self.img = ImageTk.PhotoImage(Image.open("output/heightmap.tif"))
        self.image_on_canvas = self.canvas.create_image(20, 20, anchor=NW, image=self.img)

        self.canvas2 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas2.pack(side=LEFT)
        self.img2 = ImageTk.PhotoImage(Image.open("output/watermap.tif"))
        self.image_on_canvas2 = self.canvas2.create_image(20, 20, anchor=NW, image=self.img2)

        self.canvas3 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas3.pack(side=LEFT)
        self.img3 = ImageTk.PhotoImage(Image.open("output/texturemap.tif"))
        self.image_on_canvas3 = self.canvas3.create_image(20, 20, anchor=NW, image=self.img3)

        self.label_c = Label(self.con2,text="Coarse Styles", font=controller.fontePadrao)
        self.label_c.pack()
        self.label_c["font"] = controller.fontePadrao
        self.label_c.pack(side=LEFT)
        self.variable_c = StringVar(self)
        self.variable_c.set(options[0]) # default value
        self.w_c = OptionMenu(self.con2, self.variable_c, *options)
        self.w_c["width"] = 50
        self.w_c.pack(side=LEFT)

        self.label_m = Label(self.con3,text="Middle Styles", font=controller.fontePadrao)
        self.label_m.pack()
        self.label_m["font"] = controller.fontePadrao
        self.label_m.pack(side=LEFT)
        self.variable_m = StringVar(self)
        self.variable_m.set(options[0]) # default value
        self.w_m = OptionMenu(self.con3, self.variable_m, *options)
        self.w_m["width"] = 50
        self.w_m.pack(side=LEFT)

        self.label_f = Label(self.con4,text="Fine Styles  ", font=controller.fontePadrao)
        self.label_f.pack()
        self.label_f["font"] = controller.fontePadrao
        self.label_f.pack(side=LEFT)
        self.variable_f = StringVar(self)
        self.variable_f.set(options[0]) # default value
        self.w_f = OptionMenu(self.con4, self.variable_f, *options)
        self.w_f["width"] = 50
        self.w_f.pack(side=LEFT)

        self.l_water = Label(self.conwater,text="Water Height  ", font=controller.fontePadrao)
        self.l_water.pack(side=LEFT)
        self.waterheight = Entry(self.conwater)
        self.waterheight.insert(END,'0.3')
        self.waterheight["width"] = 10
        self.waterheight["font"] = controller.fontePadrao
        self.waterheight.pack(side=LEFT)

        self.gerar = Button(self.con5)
        self.gerar["text"] = "Generate Terrain"
        self.gerar["font"] = ("Calibri", "8")
        self.gerar["width"] = 12
        self.gerar["command"] = self.generateTerrain
        self.gerar.pack(side=RIGHT)

        button = Button(self, text="Back to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def generateTerrain(self):
        biome_c = biome_nicks[self.variable_c.get()]
        biome_m = biome_nicks[self.variable_m.get()]
        biome_f = biome_nicks[self.variable_f.get()]
        water_height = float(self.waterheight.get())

        hm.createHM_SM(biome_c,biome_m,biome_f)
        wa.createWaterMap(water_height)
        te.createTextureMap(biome_f)

        updateImages(self)

class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Biome Oriented Terrain Generation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        self.con4 = Frame(self)
        self.con4["padx"] = 10
        self.con4["pady"] = 10
        self.con4.pack()
        self.label_f = Label(self.con4,text="Biome  ", font=controller.fontePadrao)
        self.label_f.pack()
        self.label_f["font"] = controller.fontePadrao
        self.label_f.pack(side=LEFT)
        self.variable_f = StringVar(self)
        self.variable_f.set(options[0]) # default value
        self.w_f = OptionMenu(self.con4, self.variable_f, *options)
        self.w_f["width"] = 50
        self.w_f.pack(side=LEFT)

        self.conwater = Frame(self)
        self.conwater["padx"] = 10
        self.conwater["pady"] = 10
        self.conwater.pack()
        self.l_water = Label(self.conwater,text="Water Height  ", font=controller.fontePadrao)
        self.l_water.pack(side=LEFT)
        self.waterheight = Entry(self.conwater)
        self.waterheight.insert(END,'0.3')
        self.waterheight["width"] = 10
        self.waterheight["font"] = controller.fontePadrao
        self.waterheight.pack(side=LEFT)

        self.con5 = Frame(self)
        self.con5["padx"] = 10
        self.con5["pady"] = 10
        self.con5.pack()
        self.gerar = Button(self.con5)
        self.gerar["text"] = "Generate Terrain"
        self.gerar["font"] = ("Calibri", "8")
        self.gerar["width"] = 12
        self.gerar["command"] = self.generateTerrain
        self.gerar.pack(side=RIGHT)


        self.con_images = Frame(self)
        self.con_images["padx"] = 10
        self.con_images["pady"] = 10
        self.con_images.pack()

        self.canvas4 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas4.pack(side=LEFT)
        self.img4 = ImageTk.PhotoImage(Image.open("output/heightmap_initial.tif"))
        self.image_on_canvas4 = self.canvas4.create_image(20, 20, anchor=NW, image=self.img4)

        self.canvas = Canvas(self.con_images, width = 200, height = 200)
        self.canvas.pack(side=LEFT)
        self.img = ImageTk.PhotoImage(Image.open("output/heightmap.tif"))
        self.image_on_canvas = self.canvas.create_image(20, 20, anchor=NW, image=self.img)

        self.canvas2 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas2.pack(side=LEFT)
        self.img2 = ImageTk.PhotoImage(Image.open("output/watermap.tif"))
        self.image_on_canvas2 = self.canvas2.create_image(20, 20, anchor=NW, image=self.img2)

        self.canvas3 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas3.pack(side=LEFT)
        self.img3 = ImageTk.PhotoImage(Image.open("output/texturemap.tif"))
        self.image_on_canvas3 = self.canvas3.create_image(20, 20, anchor=NW, image=self.img3)


        button = Button(self, text="Back to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


    def generateTerrain(self):
        biome = biome_nicks[self.variable_f.get()]
        water_height = float(self.waterheight.get())

        hm.createHM_BO(biome)
        wa.createWaterMap(water_height)
        te.createTextureMap(biome)

        updateImages(self)

class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Biome Oriented Terrain Generation with Seed Input", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        self.con4 = Frame(self)
        self.con4["padx"] = 10
        self.con4["pady"] = 10
        self.con4.pack()
        self.label_f = Label(self.con4,text="Biome  ", font=controller.fontePadrao)
        self.label_f.pack()
        self.label_f["font"] = controller.fontePadrao
        self.label_f.pack(side=LEFT)
        self.variable_f = StringVar(self)
        self.variable_f.set(options[0]) # default value
        self.w_f = OptionMenu(self.con4, self.variable_f, *options)
        self.w_f["width"] = 50
        self.w_f.pack(side=LEFT)

        self.conwater = Frame(self)
        self.conwater["padx"] = 10
        self.conwater["pady"] = 10
        self.conwater.pack()
        self.l_water = Label(self.conwater,text="Water Height  ", font=controller.fontePadrao)
        self.l_water.pack(side=LEFT)
        self.waterheight = Entry(self.conwater)
        self.waterheight.insert(END,'0.3')
        self.waterheight["width"] = 10
        self.waterheight["font"] = controller.fontePadrao
        self.waterheight.pack(side=LEFT)

        self.conseed = Frame(self)
        self.conseed["padx"] = 10
        self.conseed["pady"] = 10
        self.conseed.pack()
        self.l_seed = Label(self.conwater,text="   Seed  ", font=controller.fontePadrao)
        self.l_seed.pack(side=LEFT)
        self.seed = Entry(self.conwater)
        self.seed.insert(END,'555')
        self.seed["width"] = 10
        self.seed["font"] = controller.fontePadrao
        self.seed.pack(side=LEFT)

        self.con5 = Frame(self)
        self.con5["padx"] = 10
        self.con5["pady"] = 10
        self.con5.pack()
        self.gerar = Button(self.con5)
        self.gerar["text"] = "Generate Terrain"
        self.gerar["font"] = ("Calibri", "8")
        self.gerar["width"] = 12
        self.gerar["command"] = self.generateTerrain
        self.gerar.pack(side=RIGHT)


        self.con_images = Frame(self)
        self.con_images["padx"] = 10
        self.con_images["pady"] = 10
        self.con_images.pack()

        self.canvas4 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas4.pack(side=LEFT)
        self.img4 = ImageTk.PhotoImage(Image.open("output/heightmap_initial.tif"))
        self.image_on_canvas4 = self.canvas4.create_image(20, 20, anchor=NW, image=self.img4)

        self.canvas = Canvas(self.con_images, width = 200, height = 200)
        self.canvas.pack(side=LEFT)
        self.img = ImageTk.PhotoImage(Image.open("output/heightmap.tif"))
        self.image_on_canvas = self.canvas.create_image(20, 20, anchor=NW, image=self.img)

        self.canvas2 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas2.pack(side=LEFT)
        self.img2 = ImageTk.PhotoImage(Image.open("output/watermap.tif"))
        self.image_on_canvas2 = self.canvas2.create_image(20, 20, anchor=NW, image=self.img2)

        self.canvas3 = Canvas(self.con_images, width = 200, height = 200)
        self.canvas3.pack(side=LEFT)
        self.img3 = ImageTk.PhotoImage(Image.open("output/texturemap.tif"))
        self.image_on_canvas3 = self.canvas3.create_image(20, 20, anchor=NW, image=self.img3)


        button = Button(self, text="Back to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


    def generateTerrain(self):
        biome = biome_nicks[self.variable_f.get()]
        water_height = float(self.waterheight.get())
        seed = int(self.seed.get())

        hm.createHM_BO(biome,seed)
        wa.createWaterMap(water_height)
        te.createTextureMap(biome)


        updateImages(self)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
