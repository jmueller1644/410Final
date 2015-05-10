var urls = Array();
$("li.g").each(function(){
  if ($(this).find("cite").text().indexOf(".") != -1 && $(this).find(".intrlu") != undefined && !$(this).hasClass("no-sep")) {
    url = $(this).find(".r a").eq(0).attr("href");
    urls.push(url);
  }
});

$.post("http://localhost:8888/urls", {sites: JSON.stringify(urls)}, function(classes) {
    var counter = 0;
    console.log(classes);
    $("li.g").each(function(){
        if ($(this).find("cite").text().indexOf(".") != -1 && $(this).find(".intrlu") != undefined && !$(this).hasClass("no-sep")) {
          var imgURL = chrome.extension.getURL("icons/");
          if (classes['results'][counter] == 0) {
            imgURL += 'red_circle.png';
          } else if (classes['results'][counter] == 1) {
            imgURL += 'green_circle.png';
          } else {
            imgURL += 'blue_circle.png';
          }

          $(this).find(".r").eq(0).parent().html("<table><tr><td>" + $(this).find(".r").eq(0).parent().html() + "</td><td>" + '<img src="' + imgURL +'" alt="green"></td></tr></table>');
          counter++;
        }
    });
  });