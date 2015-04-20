import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

class WidgetMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
	self.width = self.engine.gfxMgr.camera.getViewport().getActualWidth()
	self.height = self.engine.gfxMgr.camera.getViewport().getActualHeight()
	self.overlayManager = ogre.OverlayManager.getSingleton()
	self.panel = self.overlayManager.createOverlayElement("Panel", "myNewPanel")
	self.panel.setMetricsMode(ogre.GMM_PIXELS)#RELATIVE_ASPECT_ADJUSTED)
        self.panel.setPosition(0, 0)
        self.panel.setDimensions(self.width, self.height)        
        self.panel.setMaterialName("ECSLENT/UI")
        
	self.overlay = self.overlayManager.create("myOverlay")
	self.overlay.add2D(self.panel)
	self.overlay.show()
	self.panel.show()

    def tick(self, dt):
	self.width = self.engine.gfxMgr.camera.getViewport().getActualWidth()
	self.height = self.engine.gfxMgr.camera.getViewport().getActualHeight()
        self.panel.setPosition(0,0)
        self.panel.setDimensions(self.width,self.height)

    def stop(self):
        pass

