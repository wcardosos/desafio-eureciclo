function changeFilenameSpan(event) {
  const filenameSpan = document.getElementsByClassName('file-name')[0];
  
  filenameSpan.textContent = event.target.files[0].name;
}

const inputFile = document.getElementsByClassName('file-input')[0];

inputFile.addEventListener('change', changeFilenameSpan, false);
