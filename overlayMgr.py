import ogre.renderer.OGRE as ogre

class OverlayMgr:
    def __init__(self, engine):
        self.engine = engine

    def init(self):
        self.overlayMgr = False
        self.showMenu = True

    def displayMainMenu(self):
        self.entityMgr = self.engine.entityMgr

        # Load the font
        font = ogre.FontManager.getSingleton().getResourceIterator()

        while ( font.hasMoreElements() ):
            font.getNext().load()

        self.overlayMgr = ogre.OverlayManager.getSingleton()

        # Create an overlay
        self.overlay = self.overlayMgr.create("MainOverlay")

        # Create a panel
        self.panel = self.overlayMgr.createOverlayElement("Panel", "Menu")
        self.panel.setPosition(0, 0)
        self.panel.setDimensions(1, 1)
        #self.panel.setMaterialName("spacePlane2")

        #  Create a button panel
        self.panel2 = self.overlayMgr.createOverlayElement("Panel", "Buttons")
        self.panel2.setPosition(.363, .5)
        self.panel2.setDimensions(.25, .35)
        #self.panel2.setMaterialName("Panelz")

        # Create Instructions Panel
        self.panel4 = self.overlayMgr.createOverlayElement("Panel", "InstructionScreen")
        self.panel4.setPosition(.118, .12)
        self.panel4.setDimensions(.75, .75)
        #self.panel4.setMaterialName("Instructions")

        # Create Credits Panel
        self.panel5 = self.overlayMgr.createOverlayElement("Panel", "CreditScreen")
        self.panel5.setPosition(.118, .12)
        self.panel5.setDimensions(.75, .75)
        #self.panel5.setMaterialName("Credits")

        # Title
        self.text = self.overlayMgr.createOverlayElement("TextArea", "Title")
        self.text.setPosition(.15, .15)
        self.text.setDimensions(1, 1)
        self.text.setCaption("Tank Warfare")
        self.text.setCharHeight(.1)
        self.text.setFontName("StarWars")
        self.text.setColourTop((0.05, 0.05, 0.05))
        self.text.setColourBottom((0.7, 0.7, 0.9))
        self.panel.addChild(self.text)

        # Start Button
        self.text = self.overlayMgr.createOverlayElement("TextArea", "Start")
        self.text.setPosition(0.07, 0.05)
        self.text.setDimensions(1, 1)
        self.text.setCaption("Start Game")
        self.text.setCharHeight(.025)
        self.text.setFontName("StarWars")
        self.text.setColour(( 1, 1, 1 ))
        self.text.setSpaceWidth(.01)
        self.panel2.addChild(self.text)

        # Instructions Button
        self.text = self.overlayMgr.createOverlayElement("TextArea", "Instructions")
        self.text.setPosition(0.07, 0.1)
        self.text.setDimensions(1, 1)
        self.text.setCaption("Instructions")
        self.text.setCharHeight(.025)
        self.text.setFontName("StarWars")
        self.text.setColour(( 1, 1, 1 ))
        self.text.setSpaceWidth(.01)
        self.panel2.addChild(self.text)

        # Credits Button
        self.text = self.overlayMgr.createOverlayElement("TextArea", "Credits")
        self.text.setPosition(0.07, 0.15)
        self.text.setDimensions(1, 1)
        self.text.setCaption("Credits")
        self.text.setCharHeight(.025)
        self.text.setFontName("StarWars")
        self.text.setColour(( 1, 1, 1 ))
        self.text.setSpaceWidth(.01)
        self.panel2.addChild(self.text)

        # Add the panel to the overlay
        self.overlay.add2D(self.panel)
        self.overlay.add2D(self.panel2)
        self.overlay.add2D(self.panel4)
        self.overlay.add2D(self.panel5)

        # Show the overlay
        self.overlay.show()

        instructions = self.overlayMgr.getOverlayElement("InstructionScreen")
        instructions.hide()

        credits = self.overlayMgr.getOverlayElement("CreditScreen")
        credits.hide()

    def tick(self, dt):

        if self.engine.inputMgr.startCheck == True:
            buttons = self.overlayMgr.getOverlayElement("Buttons")
            menu = self.overlayMgr.getOverlayElement("Menu")
            menu.hide()
            buttons.hide()
            self.overlay.hide()
            self.showMenu = False
            self.engine.controlMgr.initTanks()

        if self.engine.inputMgr.instructionsCheck == True and self.engine.inputMgr.startCheck == False:
            instructions = self.overlayMgr.getOverlayElement("InstructionScreen")
            instructions.show()
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement("Buttons")
            buttons.hide()

        if self.engine.inputMgr.creditsCheck == True and self.engine.inputMgr.startCheck == True:
            credits = self.overlayMgr.getOverlayElement("CreditScreen")
            credits.show()
            buttons = self.engine.guiMgr.overlayMgr.getOverlayElement("Buttons")
            buttons.hide()
