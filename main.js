let car = document.querySelector("#car");
let data = [
  {
    img: "https://top-tuning.ru/upload/images/news/101120/Ferrari-488-GTB-Novitec-Rosso-7.jpg",
    title: "Novitec Rosso Ferrari",
    Price: "$350 000",
  },
  {
    img: "https://avatars.mds.yandex.net/get-mpic/6458782/img_id1711733119337088701.jpeg/orig",
    title: "Mercedes GT3 AMG",
    Price: "$1,135,642",
  },
  {
    img: "https://i.pinimg.com/originals/32/3b/da/323bdaee469ddcab3872229458e0a58a.jpg",
    title: "Bugatti Chiron",
    Price: "$3,300,000",
  },
  {
    img: "https://garagedreams.net/wp-content/uploads/2018/12/Where-to-find-a-toyota-supra-for-sale.jpg",
    title: "Supra mk4",
    Price: "$80,483.",
  },
  {
    img: "https://tuningmode.ru/sites/default/files/pol_pl_splitter-przedni-v-3-toyota-supra-mk5-8885_3.jpg",
    title: "Supra mk5",
    Price: "$60,535",
  },
  {
    img: "https://i.ytimg.com/vi/Ndp3k4iDz1A/maxresdefault.jpg",
    title: "BMW M3",
    Price: "$86,475",
  },
  {
    img: "https://www.zastavki.com/pictures/2560x1600/2011/Auto_Citroen_Citroen_sport_car_028068_.jpg",
    title: "Citroen new model",
    Price: "$4,576,000",
  },
  {
    img: "https://avatars.mds.yandex.net/i?id=eff8f059f3cf42c9f327039b226faa9d_l-7549266-images-thumbs&n=13",
    title: "Moster Raptor Cubey",
    Price: "$700,000",
  },
];
for (let item of data) {
  car.innerHTML += ` <article class="border rounded-lg bg-white overflow-hidden">
<img class="w-full h-44 object-cover" src="${item.img}" alt="" />
<div class="p-2">
<h1 class="text-lg font-medium text-gray-900">${item.title}</h1>
<h2 class="text-blue-500 font-bold text-xl my-1">${item.Price}</h2>
<button
class="bg-gray-900 text-white p-1 w-full rounded-md mt-2 active:scale-95 duration-300"
>
Add to Cart
</button>
</div>
</article>`;
}
