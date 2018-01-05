from binaryninja import *

"""
BlackHighlightColor = <HighlightStandardColor.BlackHighlightColor: 9>
BlueHighlightColor = <HighlightStandardColor.BlueHighlightColor: 1>
CyanHighlightColor = <HighlightStandardColor.CyanHighlightColor: 3>
GreenHighlightColor = <HighlightStandardColor.GreenHighlightColor: 2>
MagentaHighlightColor = <HighlightStandardColor.MagentaHighlightColor: 5>
NoHighlightColor = <HighlightStandardColor.NoHighlightColor: 0>
OrangeHighlightColor = <HighlightStandardColor.OrangeHighlightColor: 7>
RedHighlightColor = <HighlightStandardColor.RedHighlightColor: 4>
WhiteHighlightColor = <HighlightStandardColor.WhiteHighlightColor: 8>
YellowHighlightColor = <HighlightStandardColor.YellowHighlightColor: 6>
"""
color_picker = {
	'White': HighlightStandardColor.WhiteHighlightColor,
	'Black': HighlightStandardColor.BlackHighlightColor,
	'Magenta': HighlightStandardColor.MagentaHighlightColor,
	'Blue': HighlightStandardColor.BlueHighlightColor,
	'Cyan': HighlightStandardColor.CyanHighlightColor,
	'Green': HighlightStandardColor.GreenHighlightColor,
	'Orange': HighlightStandardColor.OrangeHighlightColor,
	'Yellow': HighlightStandardColor.YellowHighlightColor,
	'No': HighlightStandardColor.NoHighlightColor,
}
color_picker_order = ['White', 'Black', 'Magenta', 'Blue', 'Cyan', 'Green', 'Orange', 'Yellow', 'No']

def do_highlight_trace(bv, function):
	global color_picker, color_picker_order
	tex_f = MultilineTextField("Trace (List of Executed Instruction)")
	choice_f = ChoiceField("Highlight Color", color_picker_order)
	ret = get_form_input(["Trace", None, tex_f, choice_f], "Trace Highlighter")
	color = color_picker_order[choice_f.result]
	str_trace = tex_f.result
	trace = [int(x, 16) for x in str_trace.split('\n')]
	for addr in trace:
		bbs = bv.get_basic_blocks_at(addr)
		for bb in bbs:
			plugin.log.log_info("hilighting BasicBlock %r (addr=%#x) with %s" % (bb, addr, color))
			bb.highlight = color_picker[color]
	

PluginCommand.register_for_address("Highlight Trace", "Highlight Trace", do_highlight_trace)
