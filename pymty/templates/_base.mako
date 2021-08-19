<!doctype html>
<html class="no-js" lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="theme-color" content="#2b5b84">
% if title:
    <title>${title} - Python Monterrey</title>
% else:
    <title>Python Monterrey</title>
% endif
    <meta name="description" content="Grupo de usuarios de Python en Monterrey">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1,user-scalable=no">
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/main.css">
    <script src="/static/js/vendor/modernizr-2.6.2.min.js"></script>
    <link rel="stylesheet" href="/static/rmm-css/responsivemobilemenu.css" type="text/css"/>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/vendor/jquery-1.10.2.min.js"><\/script>')</script>
    <script src="/static/rmm-js/responsivemobilemenu.js"></script>
  </head>
  <body>
    <!--[if lt IE 8]>
        <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
    <div id="container">
      <div id="top">
        <header>
          <div id="logo">
            <a href="/" alt="Python Monterrey/ Inicio">
              <img src="/static/img/pymty-logo.svg" alt="Python Monterrey" style="width: 15em">
            </a>
          </div>
          <div class="rmm"  data-menu-title="Men&uacute;" data-menu-style="sapphire" id="menu">
            <ul>
              <li>
                <a href="/reuniones">Reuniones</a>
              </li>
              <li>
                <a href="/documentacion">Documentación</a>
              </li>
              <li>
                <a href="/contribuir">
                  Contribuir
                </a>
              </li>
              <li>
                <a href="/trabajos">Bolsa de trabajo</a>
              </li>
              <li>
                <a href="http://blog.pymty.org/" target="_blank"> Blog </a>
              </li>
            </ul>
          </div>
        </header>
      </div>
      <div id="content">
        ${next.body()}
      </div>
      <div id="bottom">
        <footer>
          <a href="https://www.meetup.com/pythonmty/">Meetup</a>
          <a href="https://www.facebook.com/groups/pymty/">Facebook</a>
          <a href="http://twitter.com/pymty">Twitter</a>
          <a href="http://webchat.freenode.net/?channels=pymty">IRC</a>
          <a href="https://groups.google.com/forum/#!forum/pymty">Google group</a>
          <a href="https://www.python.org/">Sitio oficial de Python</a>
        </footer>
      </div>
    </div>
    <script src="/static/js/plugins.js"></script>
    <script src="/static/js/main.js"></script>
    <script>
      (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
      function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
      e=o.createElement(i);r=o.getElementsByTagName(i)[0];
      e.src='//www.google-analytics.com/analytics.js';
      r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
      ga('create','UA-3765019-16','auto');ga('send','pageview');
    </script>
  </body>
</html>
