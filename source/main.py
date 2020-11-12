from urwid import *

# define palette
palette = [("rev","black","white")]

# make borders
pile = Pile([])
borders = LineBox(pile,
    title="RF Connect",
    title_align="center")

# create all elements
instr_txt = Text("Instrument:")
instr_ddm = Text("[TCPIP::255.255.255.255::INSTR]")
reload_btn = Text("(Reload)")
rfout_txt = Text("RF Out:")
rfout_btns = Text("(   ON   ) (   OFF   )")
freq_txt = Text("Frequency:")
freq_ds = Text("123456789.123456789 [MHz]")
pow_txt = Text("Power:")
pow_ds = Text("123456789.123456789 [dBm]")
quit_btn = Text("(Quit)")
mssg = Text("Sample message.")
div = Divider()

# add all elements to pile
items = [instr_txt,instr_ddm,reload_btn,div,
        rfout_txt,rfout_btns,div,
        freq_txt,freq_ds,div,
        pow_txt,pow_ds,div,
        quit_btn,div,mssg]
for item in items:
    pile.contents.append((item,pile.options()))

# start program loop
fill = Filler(borders,"top")
loop = MainLoop(fill,palette)
loop.run()
