// Mảng chứa các đường dẫn ảnh nền
const backgrounds = [
  './images/checkout.jpg',
  './images/checkout2.jpg',
  './images/checkout3.jpg',
];
let currentBackgroundIndex = 0;
const header = document.querySelector('.header');

// Preload images to prevent delay during background switch
backgrounds.forEach((src) => {
  const img = new Image();
  img.src = src;
});

// Hàm chuyển đổi ảnh nền
function changeBackground() {
  currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
  header.style.backgroundImage = 
    `linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)), 
     url(${backgrounds[currentBackgroundIndex]})`;
}

// Chuyển đổi ảnh sau mỗi 3 giây
setInterval(changeBackground, 3000);




        const navBtn = document.querySelector("#nav-btn");
const navbar = document.querySelector("#navbar");
const navClose = document.querySelector("#nav-close");

navBtn.addEventListener("click", () => {
  navbar.classList.add("showNav");
});

navClose.addEventListener("click", () => {
  navbar.classList.remove("showNav");
});



document.getElementById('explore-btn').addEventListener('click', function(e) {
  e.preventDefault();
  // Cuộn mượt đến phần story
  document.querySelector('#story').style.display = 'block'; // Hiển thị phần story
  document.querySelector('#story').scrollIntoView({ behavior: 'smooth' });
});


 // Hàm reset về trạng thái ban đầu
 function resetToInitial() {
  // Ẩn toàn bộ các trang câu chuyện
  var storyPages = document.querySelectorAll('.story-content');
  storyPages.forEach(function(page) {
    page.classList.remove('active');
  });

  // Ẩn phần câu chuyện và hiện lại nút "Cùng khám phá"
  document.querySelector('.banner-title').style.display = 'block'; // Hiển thị tiêu đề lại
  document.querySelector('.banner-btn').style.display = 'block';  // Hiển thị nút "Cùng khám phá"
  document.querySelector('.story').style.display = 'none'; // Ẩn phần câu chuyện
}

// Hàm hiển thị các phần của câu chuyện
function showStory(pageId) {
  // Ẩn toàn bộ các trang trước khi hiển thị trang mới
  var storyPages = document.querySelectorAll('.story-content');
  storyPages.forEach(function(page) {
    page.classList.remove('active');
  });

  // Hiển thị trang hiện tại
  document.getElementById(pageId).classList.add('active');
  document.querySelector('.story').style.display = 'block'; // Hiển thị phần câu chuyện
}

// Thêm sự kiện cho nút "Cùng khám phá"
document.getElementById('explore-btn').addEventListener('click', function(e) {
  e.preventDefault(); // Ngăn hành vi mặc định của thẻ <a>
  showStory('page1');
  document.querySelector('.banner-title').style.display = 'none'; // Ẩn tiêu đề chính
  document.querySelector('#explore-btn').style.display = 'none'; // Ẩn nút "Cùng khám phá"
});

// Thêm sự kiện cho nút "Khám phá tiếp"
document.getElementById('continue-btn').addEventListener('click', function(e) {
  e.preventDefault(); // Ngăn hành vi mặc định của thẻ <a>
  showStory('page2');
});

// Thêm sự kiện cho nút "Quay lại"
document.getElementById('back-btn').addEventListener('click', function(e) {
  e.preventDefault(); // Ngăn hành vi mặc định của thẻ <a>
  resetToInitial(); // Reset lại trạng thái ban đầu
});

// Khởi động ban đầu
resetToInitial();


//gỡ bỏ lớp active cho thanh menu khi người dùng nhấp vào nút mở hoặc đóng.
document.getElementById('nav-btn').addEventListener('click', function() {
  document.getElementById('navbar').classList.add('active');
});

document.getElementById('nav-close').addEventListener('click', function() {
  document.getElementById('navbar').classList.remove('active');
}); 
/////////////////////////////


function showPage(pageId) {
  // Ẩn tất cả các trang
  const pages = document.querySelectorAll('.page');
  pages.forEach(page => {
    page.style.display = 'none';
  });

  // Hiển thị trang được chọn
  const selectedPage = document.getElementById(pageId);
  selectedPage.style.display = 'block';
}

// Hiển thị trang A khi trang web được tải
document.addEventListener("DOMContentLoaded", function() {
  showPage('pageA');
});


//ẩn ban đầu các sản phẩm product
function showMoreProducts() {
  var moreProducts = document.getElementById("more-products");
  var viewMoreBtn = document.getElementById("view-more");

  if (moreProducts.style.display === "none") {
    moreProducts.style.display = "block";
    viewMoreBtn.textContent = "Thu gọn"; // Đổi thành "Thu gọn" sau khi hiển thị toàn bộ sản phẩm
  } else {
    moreProducts.style.display = "none";
    viewMoreBtn.textContent = "Xem thêm"; // Đổi lại thành "Xem thêm"
  }
}

/*============  từ dòng 147 đến 258   =================*/
const API_BASE = "http://127.0.0.1:5000";
const PRODUCTS_API = API_BASE + "/api/products";

// biến lưu data
let productsData = [];
let showAll = false;

// build absolute image URL từ giá trị DB (p.anh có thể là '/images/...' hoặc 'images/...' hoặc full URL)
function buildImageUrl(raw) {
  if (!raw) return API_BASE + "/images/placeholder.jpg"; // nếu có placeholder trên backend
  raw = String(raw).trim();
  // nếu đã là url đầy đủ
  if (raw.startsWith("http://") || raw.startsWith("https://")) return raw;
  // nếu bắt đầu bằng / -> nối trực tiếp vào API_BASE
  if (raw.startsWith("/")) return API_BASE + raw;
  // nếu không có / đầu (ví dụ 'images/...') -> thêm / trước
  return API_BASE + "/" + raw.replace(/^\/+/, "");
}

function formatPrice(number) {
  if (number == null) return "";
  return new Intl.NumberFormat('vi-VN').format(Number(number || 0)) + "đ";
}

function escapeHtml(text) {
  if (!text) return "";
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function productCardHTML(p) {
  // p là object đã chuẩn hóa ở fetchProducts
  const imgSrc = buildImageUrl(p.image || p.anh || "");
  const title = escapeHtml(p.title || p.tenSanPham || p.ten_san_pham || "Sản phẩm");
  const price = formatPrice(p.price || p.gia);
  const id = p.id || p.ID || "";
  const detailLink = `./Product/product.html?id=${id}`;

  return `
  <article class="product">
    <a href="${detailLink}" class="product-link">
      <img src="${imgSrc}" alt="${title}" class="product-img" loading="lazy"/>
      <span class="details-overlay">Chi tiết</span>
    </a>
    <a href="${detailLink}" class="product-link">
      <h3 class="product-title">${title}</h3>
    </a>
    <h3 class="product-price">${price}</h3>
  </article>`;
}

function renderProducts() {
  const container = document.getElementById("products-container");
  if (!container) return;

  if (!productsData || productsData.length === 0) {
    container.innerHTML = "<p>Chưa có sản phẩm nào.</p>";
    return;
  }

  let toShow = productsData;
  if (!showAll) toShow = productsData.slice(0, 3);

  container.innerHTML = toShow.map(p => productCardHTML(p)).join("\n");

  const btn = document.getElementById("view-more");
  if (!btn) return;
  if (productsData.length <= 3) {
    btn.style.display = "none";
  } else {
    btn.style.display = "inline-block";
    btn.textContent = showAll ? "Thu gọn" : "Xem thêm";
  }
}

function showMoreProducts() {
  showAll = !showAll;
  renderProducts();
}

async function fetchProducts() {
  try {
    const res = await fetch(PRODUCTS_API);
    if (!res.ok) throw new Error(`API lỗi ${res.status}`);
    const arr = await res.json();

    // Chuẩn hóa mỗi item về shape dùng trong frontend
    productsData = arr.map(item => ({
      id: item.id,
      title: item.tenSanPham || item.title || item.name,
      price: item.gia || item.price,
      description: item.moTa || item.description,
      anh: item.anh,        // giữ raw từ DB (vd '/images/products/xxx.jpg')
      image: item.anh || item.image || ""
    }));

    renderProducts();
  } catch (err) {
    console.error("Lỗi khi gọi API products:", err);
    const container = document.getElementById("products-container");
    if (container) container.innerHTML = `<p style="color: red;">Không tải được dữ liệu sản phẩm — ${err.message}</p>`;
  }
}

// chạy khi load
document.addEventListener("DOMContentLoaded", () => {
  fetchProducts();
});

/*==========================================*/


document.getElementById("payment-method").addEventListener("change", function() {
  let bankInfo = document.getElementById("bank-info");
  let momoInfo = document.getElementById("momo-info");

  if (this.value === "bank") {
      bankInfo.style.display = "block";
      momoInfo.style.display = "none";
  } else if (this.value === "momo") {
      momoInfo.style.display = "block";
      bankInfo.style.display = "none";
  } else {
      bankInfo.style.display = "none";
      momoInfo.style.display = "none";
  }
});

document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("payment-method").addEventListener("change", function() {
      let bankInfo = document.getElementById("bank-info");
      bankInfo.style.display = this.value === "bank" ? "block" : "none";
  });

  document.getElementById("payment-form").addEventListener("submit", function(event) {
      event.preventDefault();

      let name = document.getElementById("name").value;
      let phone = document.getElementById("phone").value;
      let address = document.getElementById("address").value;
      let paymentMethod = document.getElementById("payment-method").value;

      alert(`Cảm ơn bạn ${name}! Đơn hàng của bạn sẽ sớm được xử lý.\nSố điện thoại: ${phone}\nĐịa chỉ: ${address}\nPhương thức thanh toán: ${paymentMethod}`);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  let bankInfo = document.getElementById("bank-info");
  let momoInfo = document.getElementById("momo-info");

  // Ẩn tất cả phương thức thanh toán ban đầu
  bankInfo.style.display = "none";
  momoInfo.style.display = "none";

  document.getElementById("payment-method").addEventListener("change", function() {
    if (this.value === "bank") {
        bankInfo.style.display = "flex";  // Hiển thị theo kiểu flex
        momoInfo.style.display = "none";  // Ẩn momo
    } else if (this.value === "momo") {
        momoInfo.style.display = "flex";  // Hiển thị momo
        bankInfo.style.display = "none";  // Ẩn ngân hàng
    } else {
        bankInfo.style.display = "none";  // Ẩn cả hai khi không chọn gì
        momoInfo.style.display = "none";
    }
  });
});