CSeer (Colour Seer)
===================

Colour Seer overlays shows you what your screen would look like to people with
various forms of colour blindness. It is useful for designing presentations or
papers for figures.

Use
---
Just run the program. Press any key to quit.

To facilitate running the program, I add the following to my `~/.config/openbox/lubuntu-rc.xml` file.

    <keybind key="W-C">
      <action name= "Execute" >
        <execute>/home/my_user/bin/cseer</execute>
      </action>
    </keybind>

Roadmap
-------
At the moment only grayscale viewing is supported. I intend to add other forms
of colour blindness soon.