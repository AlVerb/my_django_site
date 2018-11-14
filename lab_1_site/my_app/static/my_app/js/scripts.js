function openBox(title, text, date) {
  console.log(title, text , date);
  $('.full_title_note').html(title);
  $('.full_text_note').html(text);
  $('.full_date_note').html(date);
  display = document.getElementById('note').style.display;
  if(display == 'none'){
    document.getElementById('note').style.display = 'block';
  }
}

function closeBox() {
  display = document.getElementById('note').style.display;
  if(display == 'block'){
    document.getElementById('note').style.display = 'none';
  }
}
