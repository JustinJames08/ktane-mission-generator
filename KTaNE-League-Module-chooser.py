import json
from tkinter import filedialog
from tkinter import *
import random
import os

modules=[]
finalmodules=[]
def loadjson():
	root.filename =  filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = (("JSON files","*.json"),("all files","*.*")))
	
def generate():
	modules=[]
	finalmodules=[]
	with open(root.filename, "r") as read_file:
		data = json.load(read_file)
		for p in data['modules']:
			modules.append(p)
		
	for i in range(int(tb.get())):
		rnd=random.randint(0,(len(modules))-1)
		finalmodules.append(modules[rnd])
		del modules[rnd]
	#print(modules,finalmodules)
	print("JSON pared, generating...")
	f=open("Mission.asset.meta.txt","w+")
	f.write("fileFormatVersion: 2\n")
	f.write("guid: a9016cf977d3745cfa3d11fd591c988a\n")
	f.write("timeCreated: 1560511875\n")
	f.write("licenseType: Free\n")
	f.write("NativeFormatImporter:\n")
	f.write("  externalObjects: {}\n")
	f.write("  mainObjectFileID: 11400000\n")
	f.write("  userData: \n")
	f.write("  assetBundleName: mod.bundle\n")
	f.write("  assetBundleVariant: \n")
	f.close()
	os.rename('Mission.asset.meta.txt', 'Mission.asset.meta')
	
	
	
	g=open("Mission.asset.txt","w+")
	g.write("%YAML 1.1\n")
	g.write("%TAG !u! tag:unity3d.com,2011:\n")
	g.write("--- !u!114 &11400000\n")
	g.write("MonoBehaviour:\n")
	g.write("  m_ObjectHideFlags: 0\n")
	g.write("  m_PrefabParentObject: {fileID: 0}\n")
	g.write("  m_PrefabInternal: {fileID: 0}\n")
	g.write("  m_GameObject: {fileID: 0}\n")
	g.write("  m_Enabled: 1\n")
	g.write("  m_EditorHideFlags: 0\n")
	g.write("  m_Script: {fileID: -548183353, guid: 45b809be76fd7a3468b6f517bced6f28, type: 3}\n")
	g.write("  m_Name: Mission\n")
	g.write("  m_EditorClassIdentifier: \n")
	g.write("  DisplayName: Mission\n")
	g.write("  Description: A mission generated from a json file\n")
	g.write("  GeneratorSetting:\n")
	g.write("    TimeLimit: 3000\n")
	g.write("    NumStrikes: 3\n")
	g.write("    TimeBeforeNeedyActivation: 60\n")
	g.write("    FrontFaceOnly: 0\n")
	g.write("    OptionalWidgetCount: 5\n")
	g.write("    ComponentPools:\n")
	
	
	
	
	
	
	for i in finalmodules:
		temp="      - "
		temp2=i
		temp3="\n"
		temp4=temp,temp2,temp3
		finaltemp=''.join(temp4)
		g.write("    - Count: 1\n")
		g.write("      AllowedSources: 2\n")
		g.write("      ComponentTypes: \n")
		g.write("      SpecialComponentType: 0\n")
		g.write("      ModTypes:\n")
		g.write(finaltemp)
	g.write("  PacingEventsEnabled: 1\n")
	g.close()
	os.rename('Mission.asset.txt', 'Mission.asset')
	print("Generation succeed!")
	
root = Tk()

ld = Button(text ="Load json", command = loadjson)
tb = Entry()
gen = Button(text ="Generate", command = generate)

ld.pack()
tb.pack()
gen.pack()
root.mainloop()
