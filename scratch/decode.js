const str = "‹TÖ";
for (let i = 0; i < str.length; i++) {
  console.log(str[i], str.charCodeAt(i).toString(16).toUpperCase());
}
