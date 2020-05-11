import c4d, os

def main():
    
    fn = "preset://adaptive primitives.lib4d/capsule" #.c4d"

    doc.StartUndo() # Start recording undos
    flags = c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS | c4d.SCENEFILTER_MERGESCENE # Merge objects and materials
    
    c4d.documents.MergeDocument(doc, fn, flags)
    
    c4d.EventAdd() # Refresh Cinema 4D
    doc.EndUndo() # Stop recording undos

    
if __name__=='__main__':
    main()