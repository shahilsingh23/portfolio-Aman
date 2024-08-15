import streamlit as st

# Hide the Streamlit interface with custom CSS
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# HTML content as a string
html_content = """
<!DOCTYPE html>
<html>
    <head>
        <title>@cine.aman</title>
        <link rel="shortcut icon" href="./icon.png" type="image/x-icon">
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/locomotive-scroll@3.5.4/dist/locomotive-scroll.css">
    </head>
    <body>
        <div id="loader"> 
            <h1>Come</h1>
            <h1>With </h1>
            <h1>Me</h1>
            <h1>@cineaman</h1>
        </div>
        
        <div id="fixed"> </div>
        <div id="main">
          <div id="page1">
            <nav>
                <img src="https://uploads-ssl.webflow.com/64d3dd9edfb41666c35b15b7/64d3dd9edfb41666c35b15c2_Sundown%20logo.svg">
                <div class ="anchor">
                    <a href="https://www.instagram.com/cine.aman/"> Instagram </a> 
                    <a href="https://www.youtube.com/@whoaman3526"> Youtube </a> 
                    <a href="https://www.instagram.com/a.mansing/"> About </a> 
                </div>
            </nav>

            <div id="center">
                <div id="left">
                    <h3> It is a multi-disciplinary studio focused on creating a unique videos and photos </h3>
                </div>
                <div id="right">
                    <h1> COME WITH <br> US MAKE <br> YOU A PERFECT </h1>
                </div>
            </div>
            <div>
                <video autoplay mute loop src="https://sheryislive.github.io/sundown/video.mp4"> </video>
            </div>
          </div>

          <div id="page2">
            <div id="moving-text">
                <div class="con"> 
                    <div id="hi"> </div>
                    <h1>Photography</h1>
                    <div id="hi"> </div>
                    <h1>Cinematography</h1>
                    <div id="hi"> </div>
                    <h1>Content</h1>
                    <div id="hi"> </div>
                    <h1>Editing</h1>
                </div>
                <div class="con"> 
                    <div id="hi"> </div>
                    <h1>Photography</h1>
                    <div id="hi"> </div>
                    <h1>Cinematography</h1>
                    <div id="hi"> </div>
                    <h1>Content</h1>
                    <div id="hi"> </div>
                    <h1>Editing</h1>
                </div>
                <div class="con"> 
                    <div id="hi"> </div>
                    <h1>Photography</h1>
                    <div id="hi"> </div>
                    <h1>Cinematography</h1>
                    <div id="hi"> </div>
                    <h1>Content</h1>
                    <div id="hi"> </div>
                    <h1>Editing</h1>
                </div>
            </div>

            <div id="page2-bottom">
                <h1>We are a group of design-driven,<br> goal-focused creators, producers, <br> and designers who believe that<br> the details make all the difference.<br>and we provide a content.</h1>
                <div id="page2-bottom-part">
                    <img src="https://i.ibb.co/cytMSpj/Screenshot-2024-08-07-122400.png">
                    <p>We love to create, we love to shoot, we love to collaborate, and we love to turn amazing ideas into reality. We’re here to partner with you through every step of the process and know that relationships are the most important things we build. </p>
                </div>
            </div>
          </div>

          <div id="page3">
            <div id="elem-container">
                <div id="elem-1" class="elem" data-image="https://i.ibb.co/yPyPXMy/class.png"> 
                    <div class="overlay"></div>
                    <h2>Aman singh</h2>
                </div>
                <div id="elem-2" class="elem" data-image="https://i.ibb.co/ZLtcGTC/aman-project.png"> 
                    <div class="overlay"></div>
                    <h2>Project</h2>
                </div>
                <div id="elem-3" class="elem" data-image="https://i.ibb.co/LZrgYSq/studio.png"> 
                    <div class="overlay"></div>
                    <h2>Studio</h2>
                </div>
                <div id="elem-4" class="elem" data-image="https://i.ibb.co/JKSLYdr/aman-g.pngg"> 
                    <div class="overlay"></div>
                    <h2>Creator</h2>
                </div>
                <div id="elem-5" class="elem" data-image="https://i.ibb.co/yPyPXMy/class.png"> 
                    <div class="overlay"></div>
                    <h2>Cinematography</h2>
                </div>
                <div id="elem-6" class="elem" data-image="https://i.ibb.co/XCrYvRP/cretor.png"> 
                    <div class="overlay"></div>
                    <h2>Editing</h2>
                </div>
            </div>
          </div>

          <div id="page4">
            <div id="p1">
                <h1> Photography <br> Project <br>Editing  </h1>
                <h4> My aim to perfect you<br> and gives a better <br>experience to client.</h4>
            </div>
            <div id="p2">
              <img src="https://i.ibb.co/0G83h5V/h.png";>
            </div>
          </div>

          <div id="page41">
            <div class="swiper mySwiper">
                <div class="swiper-wrapper">
                  <div class="swiper-slide"> <img src="https://i.ibb.co/28JLyxz/c.png"></div>
                  <div class="swiper-slide"><img src="https://i.ibb.co/HYCfmjr/g.png"></div>
                  <div class="swiper-slide"><img src="https://i.ibb.co/jfTrd84/f.png"></div>
                  <div class="swiper-slide"><img src="https://i.ibb.co/JsT0vVn/e.png"></div>
                  <div class="swiper-slide"><img src="https://i.ibb.co/PYZdc5s/d.png"></div>
                  <div class="swiper-slide"><img src="https://i.ibb.co/8mKg6jW/b.png"></div>
                  <div class="swiper-slide"><img src="https://i.ibb.co/p19RNFv/a.png"></div>
                </div>
                <div class="swiper-button-next"></div>
                <div class="swiper-button-prev"></div>
                <div class="swiper-pagination"></div>
                <div class="autoplay-progress">
                  <svg viewBox="0 0 48 48">
                    <circle cx="24" cy="24" r="20"></circle>
                  </svg>
                  <span></span>
                </div>
            </div>
          </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/locomotive-scroll@3.5.4/dist/locomotive-scroll.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
        <script src="logic.js"> </script>
    </body>
</html>
"""

# Display the HTML content in Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)
