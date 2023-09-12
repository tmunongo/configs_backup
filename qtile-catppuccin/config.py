# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget.battery import Battery, BatteryState
from libqtile import hook, qtile
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

mod = "mod4"
terminal = guess_terminal()

# Define your Catpuccino color scheme as a dictionary
catpuccino_colors = {
    "background": "#1E1E2E",
    "background2": "#81A1C1",
    "background2pale": "#ADC2D7",
    "foreground": "#CAA9E0",
    "accent1": "#353446",
    "accent2": "#ff0000",
    "accent3": "#ffffff",
    "accent4": "#9E4827"
}

# Define the transparency level (alpha channel) for the background color
transparency_level = 150  # You can adjust this value as needed

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    ## CUSTOM
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key([mod, "shift"], "e", lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu"), desc="Launch power menu"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -q set 5%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -q set 5%-"), desc='brightness Down'),
    Key([mod],"e", lazy.spawn("thunar"), desc='file manager'),
	Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
# layout variables
focus_stack_A = catpuccino_colors["background"]
focus_stack_B = catpuccino_colors["foreground"]
var_gap_top = 5
var_gap_bottom = 5
var_gap_left = 5
var_gap_right = 5
var_margin=[5,5,5,5]

layouts = [
    layout.Columns(
        border_focus_stack=[catpuccino_colors["foreground"], catpuccino_colors["background2"]], 
        border_focus = catpuccino_colors["foreground"],
        border_normal = catpuccino_colors['background'],
        border_width=4, 
        margin=var_margin,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    layout.RatioTile(),
    layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


# Define Nerd Fonts icon for the battery
nf_icons = {
    "battery": "\uf578",
}

### VOLUME

class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ' 婢 '
        elif self.volume <= 33:
            self.text = '  '
        elif self.volume < 66:
            self.text = ' 墳 '
        else:
            self.text = '  '
 
    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ' 婢 '
        elif self.volume <= 33:
            self.text = '  '
        elif self.volume < 66:
            self.text = ' 墳 '
        else:
            self.text = '  '
        self.draw()
 
        if wob:
            with open(self.wob, 'a') as f:
                 f.write(str( self.volume) + "\n")


# Functions
volume = MyVolume(
    format = '{percent:2.0%} {char}',
    fontsize = 15,
    padding=2,
    font="JetBrainsMonoExtraBold Nerd Font",
    foreground=catpuccino_colors["accent1"],
    background=catpuccino_colors["foreground"],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

## BATTERY

class MyBattery(Battery):
    def build_string(self, status):
        if self.layout is not None:
            if status.state == BatteryState.DISCHARGING and status.percent < self.low_percentage:
                self.layout.colour = self.low_foreground
            else:
                self.layout.colour = self.foreground
        if status.state == BatteryState.DISCHARGING:
            if status.percent >= 0.90:
                char = ''
            elif status.percent >= 0.80:
                char = ''
            elif status.percent >= 0.70:
                char = ''
            elif status.percent >= 0.60:
                char = ''
            elif status.percent >= 0.50:
                char = ''
            elif status.percent >= 0.40:
                char = ''
            elif status.percent >= 0.30:
                char = ''
            elif status.percent >= 0.20:
                char = ''
            elif status.percent >= 0.10:
                char = ' '
            else:
                char = ' '
        elif status.percent >= 1 or status.state == BatteryState.FULL:
            char = ' '
        elif status.state == BatteryState.EMPTY or \
                (status.state == BatteryState.UNKNOWN and status.percent == 0):
            char = ''
        else:
            char = ' '
        return self.format.format(char=char, percent=status.percent)
 
 
battery = MyBattery(
    format='{char} {percent:2.0%} ',
    low_foreground=catpuccino_colors["accent2"],
    show_short_text=False,
    low_percentage=0.25,
    fontsize=13,
    update_interval=15,
    font="JetBrainsMonoExtraBold Nerd Font",
    # background=colors[0],
    background=catpuccino_colors["foreground"],
    foreground=catpuccino_colors["accent1"],
    margin=[1,1,1,1]
)


# Calculate the background color with transparency
background_color = f"{catpuccino_colors['background']}{transparency_level:02X}"


screens = [
    Screen(
        top = bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    active=catpuccino_colors["foreground"],
                    inactive=catpuccino_colors["accent1"],
                    highlight_method="line",
                    this_current_screen_border=catpuccino_colors["foreground"],
                    this_screen_border=catpuccino_colors["accent1"],
                    other_current_screen_border=catpuccino_colors["foreground"],
                    other_screen_border=catpuccino_colors["background2"],
                ),
                widget.Prompt(),
                widget.Sep(
                    background=catpuccino_colors["background"],
                    foreground=catpuccino_colors["background"],
                    linewidth=10,
                    size_percent=100
                ),
                widget.Memory(
                    background=catpuccino_colors["foreground"],
                    foreground=catpuccino_colors['accent1'],
                    measure_mem='G'
                ),
                widget.Sep(
                    background=catpuccino_colors["background"],
                    foreground=catpuccino_colors["background"],
                    linewidth=10,
                    size_percent=100
                ),
                battery,
                widget.Sep(
                    background=catpuccino_colors["background"],
                    foreground=catpuccino_colors["background"],
                    linewidth=10,
                    size_percent=100
                ),
                volume,
                widget.Sep(
                    background=catpuccino_colors["background"],
                    foreground=catpuccino_colors["background"],
                    linewidth=10,
                    size_percent=100
                ),
                widget.CPUGraph(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": (catpuccino_colors["accent2"], catpuccino_colors["accent3"]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Sep(
                    background=catpuccino_colors["background"],
                    foreground=catpuccino_colors["background"],
                    linewidth=10,
                    size_percent=100
                ),
                widget.Backlight(
                    backlight_name='intel_backlight',
                    background=catpuccino_colors["foreground"],
                    foreground=catpuccino_colors["accent1"]
                ),
                widget.Sep(
                    background=catpuccino_colors["background"],
                    foreground=catpuccino_colors["background"],
                    linewidth=10,
                    size_percent=100
                ),
                # widget.Wlan(format='{essid} {percent:2.0%}', foreground=catpuccino_colors["foreground"]),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p", 
                    foreground=catpuccino_colors["accent1"],
                    background=catpuccino_colors["foreground"],
                ),
                widget.QuickExit(
                    default_text='\u23fb',
                    padding=12
                ),
            ],
            34,
            background=catpuccino_colors['background'],
            foreground=catpuccino_colors['background'],
            margin=[4, 4, 2, 4],
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
