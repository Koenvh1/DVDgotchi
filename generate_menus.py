import os


ifs = "\n".join([f"            if (g3=={i}) {{ jump vmgm menu {i + 2}; }}" for i in range(1, 46)])

content = f"""
      <pgc entry="title">
        <vob>
          <menu videoFormat="PAL" aspectRatio="1" rememberLastButton="-1">
            <svg width="720" height="540">
              <rect width="720" height="540" id="backgroundColour" style="fill:#000000;"/>
              <defs id="defs">
              </defs>
              <g id="objects"/>
              <g id="buttons">
              </g>
            </svg>
          </menu>
        </vob>
        <pre>
            g4=2;
            g5=2;
            jump vmgm menu 2;
        </pre>
      </pgc>
      <pgc>
        <vob>
          <menu videoFormat="PAL" aspectRatio="1" rememberLastButton="-1">
            <svg width="720" height="540">
              <rect width="720" height="540" id="backgroundColour" style="fill:#000000;"/>
              <defs id="defs">
              </defs>
              <g id="objects"/>
              <g id="buttons">
              </g>
            </svg>
          </menu>
        </vob>
        <pre>
            if (g4 == 0) {{ jump title 1; }} 
            if (g5 == 0) {{ jump title 1; }}
            if (g4 > 3) {{ g4=3; }}
            if (g5 > 3) {{ g5=3; }} 
            g2=random(5); 
            g3=((g2-1)*9)+((g4-1)*3)+(g5-1)+1; 
            { ifs }
        </pre>
      </pgc>"""

for idx, vid in enumerate(os.listdir("Rover\\videos")):
    content += f"""
      <pgc>
        <vob>
          <menu videoFormat="PAL" aspectRatio="1" rememberLastButton="-1">
            <svg width="720" height="540">
              <rect width="720" height="540" id="backgroundColour" style="fill:#000000;"/>
              <video width="720" height="540" preserveAspectRatio="none" id="background" xlink:href="Rover\\videos\\{vid}"/>
              <defs id="defs">
                <svg id="s_button01">
                  <defs>
                    <filter id="shadowFilter">
                      <feGaussianBlur stdDeviation="3"/>
                    </filter>
                  </defs>
                  <use x="2" y="2" id="shadow" xlink:href="#text" style="fill:#404040;fill-opacity:1;filter:url(#shadowFilter);visibility:hidden;"/>
                  <g id="gText" style="fill:#ffffff;">
                    <text x="50%" y="78%" id="text" xml:space="preserve" style="fill:#ffffff;fill-opacity:1;font-family:Arial;font-size:26;font-style:normal;font-weight:normal;text-anchor:middle;text-decoration:none;">Feed</text>
                  </g>
                  <rect x="0" y="78%" width="100%" height="2" id="underline" style="fill:none;" transform="translate(0,2)"/>
                </svg>
                <svg id="s_button02">
                  <defs>
                    <filter id="shadowFilter">
                      <feGaussianBlur stdDeviation="3"/>
                    </filter>
                  </defs>
                  <use x="2" y="2" id="shadow" xlink:href="#text" style="fill:#404040;fill-opacity:1;filter:url(#shadowFilter);visibility:hidden;"/>
                  <g id="gText" style="fill:#ffffff;">
                    <text x="50%" y="78%" id="text" xml:space="preserve" style="fill:#ffffff;fill-opacity:1;font-family:Arial;font-size:26;font-style:normal;font-weight:normal;text-anchor:middle;text-decoration:none;">Pet</text>
                  </g>
                  <rect x="0" y="78%" width="100%" height="2" id="underline" style="fill:none;" transform="translate(0,2)"/>
                </svg>
              </defs>
              <g id="objects"/>
              <g id="buttons">
                <use x="210" y="72" width="63" height="25" id="button01" xlink:href="#s_button01"/>
                <use x="466" y="72" width="44" height="25" id="button02" xlink:href="#s_button02"/>
              </g>
            </svg>
            <button id="button01" defSize="true">
              <action>g4=g4+1; jump vmgm menu 2;</action>
              <filename>text-underlined-v3.xml</filename>
              <parameter name="underlineFill" normal="none" highlighted="#ff0000" selected="#640000"/>
            </button>
            <button id="button02" defSize="true">
              <action>g5=g5+1; jump vmgm menu 2;</action>
              <filename>text-underlined-v3.xml</filename>
              <parameter name="underlineFill" normal="none" highlighted="#ff0000" selected="#640000"/>
            </button>
          </menu>
        </vob>
        <post>
            g0=random(100); 
            g1=random(100); 
            if (g0 > 90) {{ g4=g4-1; }} 
            if (g1 > 90) {{ g5=g5-1; }} 
            jump vmgm menu 2;
        </post>
      </pgc>"""

open("menus.xml", "w", encoding="utf-8").write(content)