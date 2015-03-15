# Touch Panel

An easy panel for my touch screen.

## Dependency

- `xdotool` for simulating keyboard/mouse event
- `python-tk` for UI
- `chromium-browser` for [Xiami][radio] web radio player

## Modules

### `panel.py`

A python script that generate the ui and react to user's touch envent.

Now support:

- **Modifing Monitor Brightness** by sending [XF86][xf86] keystrocks with `xdotool`.
- **Changing Display Oritation** with `xrandr`. The panel will be closed automatically after this action.
- **Xiami Music Control** using `xiami.sh`, including launch/pause/play/next of Xiami web radio player.

### `xiami.sh`

A shell script that controls Xiami Music web radio player with `xdotool`. It will launch a Xiami web radio page in `app mode` of `chromium-browser`, adjust the window's geometry and focus on the flash-player with a simulated mouse click if there isn't a such window, or toggle the play/pause status of the radio player.

If an option `-n` is given right after it,

    xiami.sh -n

it will send a `Right` keystroke to the player's window that can switch to the next song. If no player window is found, nothing will happen.

Every action will minimize the player window immediately after all operations are done.

**Note**: Actions (mainly keystrocks) that need to be sent to the web player can be failed if the flash player is not focused. A simulated click on the player is sent automatically to make that focus when the window is launched, but the focus may get lost if user have some action on the page like favoriting the artist or looking over the info. I still don't have any idea on this, and currently the best way is to prevent the lost with care. **Just remember to give a click on the blank area of that flash player after any manipulation.**

[radio]:http://www.xiami.com/radio/play/id/2
[xf86]:file:///usr/include/X11/XF86keysym.h
