// fetch("http://127.0.0.1:5000/api/track-view", {
//     method: "POST",
//     credentials: "include"
//   });
// const API_BASE = "http://127.0.0.1:5000/";

fetch("https://thanhtamtraquanp.pythonanywhere.com/api/track-view", {
    method: "POST",
    credentials: "include"
  });
const API_BASE = "https://thanhtamtraquanp.pythonanywhere.com/";



// ================= BACKGROUND  từ dòng 4 đến 52 =================
const header = document.querySelector(".header");

let backgrounds = [];
let currentBackgroundIndex = 0;

// gọi API lấy ảnh nền
async function fetchBackgrounds() {
  if (!header) return;
  try {
    const res = await fetch(API_BASE + "/api/backgrounds");
    if (!res.ok) throw new Error("Không lấy được background");

    const data = await res.json();

    // map sang url đầy đủ
    backgrounds = data.map(item => API_BASE + item.duongDan);

    if (backgrounds.length === 0) return;

    // preload
    backgrounds.forEach(src => {
      const img = new Image();
      img.src = src;
    });

    // set ảnh đầu tiên
    header.style.backgroundImage =
      `linear-gradient(rgba(0,0,0,.2), rgba(0,0,0,.2)), url(${backgrounds[0]})`;

    // chạy slideshow cứ 3 giây đổi ảnh nếu ảnh nhiều hơn 1
    setInterval(changeBackground, 3000);

  } catch (err) {
    console.error("Lỗi load background:", err);
  }
}

// đổi background
function changeBackground() {
  if (!backgrounds.length) return;
  currentBackgroundIndex =
    (currentBackgroundIndex + 1) % backgrounds.length;

  header.style.backgroundImage =
    `linear-gradient(rgba(0,0,0,.2), rgba(0,0,0,.2)), url(${backgrounds[currentBackgroundIndex]})`;
}

// chạy khi load trang
// document.addEventListener("DOMContentLoaded", fetchBackgrounds);
if (header) {
  document.addEventListener("DOMContentLoaded", fetchBackgrounds);
}

//=======================================================//

/* ================= CART LOCALSTORAGE ================= */

function getCart() {
  try {
    return JSON.parse(localStorage.getItem("cart")) || [];
  } catch {
    return [];
  }
}

function saveCart(cart) {
  localStorage.setItem("cart", JSON.stringify(cart));
  renderCart(cart);
}

function addToCart(item) {
  const cart = getCart();

  const exist = cart.find(
    p => p.id === item.id && p.type === item.type
  );

  if (exist) {
    exist.qty += item.qty;
  } else {
    cart.push(item);
  }

  saveCart(cart);
  alert("Đã thêm vào giỏ hàng!");
}

// ================= Giỏ hàng =================

function closeCart(){
  document.getElementById("cart-modal").classList.add("hidden");
}

function renderCart(cart) {
  const box = document.getElementById("cart-items");
  const totalBox = document.getElementById("cart-total");

  updateCartBadge(cart);

  if (!box || !totalBox) return;

  if (!cart || cart.length === 0) {
    box.innerHTML = "<p>Hiện chưa có sản phẩm</p>";
    if (totalBox) totalBox.textContent = "0đ";
    return;
  }

  let total = 0;

  box.innerHTML = cart.map((item, index) => {
    total += item.qty * item.price;

    return `
      <div class="cart-item">
        <div class="cart-item-left" style="display:flex;gap:10px">
          <img src="${API_BASE + item.image}">
          <div>
            <div><strong>${item.name}</strong></div>
            <div>${item.qty} × ${formatVND(item.price)}</div>
          </div>
        </div>
        <div class="cart-remove" onclick="removeCartItem(${index})">✕</div>
      </div>
    `;
  }).join("");

  if (totalBox) {
    totalBox.textContent = formatVND(total);
  }
}

function removeCartItem(index) {
  const cart = getCart();
  cart.splice(index, 1);
  saveCart(cart);
}


function showAddToCartToast(msg = "Đã thêm vào giỏ hàng") {
  let toast = document.getElementById("cart-toast");

  // nếu chưa có thì tạo
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "cart-toast";
    toast.className = "cart-toast hidden";
    document.body.appendChild(toast);
  }

  toast.textContent = "✅ " + msg;
  toast.classList.remove("hidden");
  toast.classList.add("show");

  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => toast.classList.add("hidden"), 300);
  }, 1800);
}

function toggleCart(e) {
  e.stopPropagation();
  document.getElementById("cart-modal").classList.toggle("hidden");
  renderCart(getCart());
}

// cập nhật số lượng sản phẩm đang trong giỏ 
function updateCartBadge(cart) {
  const badge = document.getElementById("cart-count");
  if (!badge) return;

  if (!cart || cart.length === 0) {
    badge.textContent = "0";
    return;
  }
  // TÍNH TỔNG SỐ LƯỢNG (qty)
  const totalQty = cart.reduce((sum, item) => {
    return sum + Number(item.qty || 0);
  }, 0);

  badge.textContent = totalQty;
}

function closeCart() {
  document.getElementById("cart-modal").classList.add("hidden");
}

/* click ra ngoài thì đóng */
document.addEventListener("click", () => {
  document.getElementById("cart-modal")?.classList.add("hidden");
});

//UPDATE BADGE KHI LOAD TRANG
document.addEventListener("DOMContentLoaded", () => {
  renderCart(getCart());
});
//=======================================================//


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
const exploreBtn = document.getElementById('explore-btn');
if (exploreBtn) {
  exploreBtn.addEventListener('click', function (e) {
    e.preventDefault();
    showStory('page1');

    const bannerTitle = document.querySelector('.banner-title');
    if (bannerTitle) bannerTitle.style.display = 'none';

    exploreBtn.style.display = 'none';
  });
}

// Thêm sự kiện cho nút "Khám phá tiếp"
const continueBtn = document.getElementById('continue-btn');
if (continueBtn) {
  continueBtn.addEventListener('click', function (e) {
    e.preventDefault();
    showStory('page2');
  });
}

// Thêm sự kiện cho nút "Quay lại"
const backBtn = document.getElementById('back-btn');
if (backBtn) {
  backBtn.addEventListener('click', function (e) {
    e.preventDefault();
    resetToInitial();
  });
}

// Khởi động ban đầu
// resetToInitial();
document.addEventListener("DOMContentLoaded", () => {
  if (document.querySelector(".story")) {
    resetToInitial();
  }
});


// function showPage(pageId) {
//   // Ẩn tất cả các trang
//   const pages = document.querySelectorAll('.page');
//   pages.forEach(page => {
//     page.style.display = 'none';
//   });

//   // Hiển thị trang được chọn
//   const selectedPage = document.getElementById(pageId);
//   selectedPage.style.display = 'block';
// }

function showPage(pageId) {
  const pages = document.querySelectorAll(".page");
  if (!pages.length) return; // 👉 KHÔNG phải trang product

  pages.forEach(p => p.style.display = "none");

  const el = document.getElementById(pageId);
  if (el) el.style.display = "block";
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

/*============  Product từ dòng 172 đến 290  =================*/
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

function formatVND(amount) {
  if (amount == null || isNaN(amount)) return "0 đ";

  return Number(amount).toLocaleString("vi-VN") + " đ";
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

// function productCardHTML(p) {
//   // p là object đã chuẩn hóa ở fetchProducts
//   const imgSrc = buildImageUrl(p.image || p.anh || "");
//   const title = escapeHtml(p.title || p.tenSanPham || p.ten_san_pham || "Sản phẩm");
//   const price = formatVND(p.price || p.gia);
//   const id = p.id || p.ID || "";
//   const detailLink = `product.html?id=${id}`;

//   return `
//   <article class="product">
//     <a href="${detailLink}" class="product-link">
//       <img src="${imgSrc}" alt="${title}" class="product-img" loading="lazy"/>
//       <span class="details-overlay">Chi tiết</span>
//     </a>
//     <a href="${detailLink}" class="product-link">
//       <h3 class="product-title">${title}</h3>
//     </a>
//     <h3 class="product-price">${price}</h3>
//   </article>`;
// }

function syncCartBadge() {
  const badge = document.getElementById("cart-count");
  if (!badge) return; // header chưa load xong

  const cart = getCart();
  const totalQty = cart.reduce((sum, item) => sum + Number(item.qty || 0), 0);
  badge.textContent = totalQty;
}

function productCardHTML(p) {
  const imgSrc = buildImageUrl(p.image || p.anh || "");
  const title = escapeHtml(p.title || p.tenSanPham || "Sản phẩm trà");
  const price = formatVND(p.price || p.gia);
  const id = p.id;

  const detailLink = `product.html?id=${id}`;

  return `
  <div class="product-card">

    <!-- CLICK ẢNH -->
    <a href="${detailLink}" class="product-link">
      <img src="${imgSrc}" alt="${title}" loading="lazy">
    </a>

    <div class="product-body">
      <div class="product-brand">Thanh Tâm Trà Quán</div>

      <!-- CLICK TÊN -->
      <a href="${detailLink}" class="product-link">
        <div class="product-name">${title}</div>
      </a>

      <div class="product-footer">
        <div class="product-price-red">${price}</div>

        <!-- NÚT + KHÔNG CHUYỂN TRANG -->
        <button class="add-btn"
          onclick='
            addToCart({
              id: ${id},
              name: "${title}",
              price: ${p.price || p.gia},
              image: "${p.image || p.anh}",
              qty: 1,
              type: "TEA"
            });
            syncCartBadge();
            showAddToCartToast();
          '>
          +
        </button>
      </div>
    </div>
  </div>
  `;
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

    // Lọc chỉ lấy sản phẩm có trạng thái ACTIVE (so sánh không phân biệt hoa thường)
    const activeOnly = arr.filter(item => {
      const status = String(item.trangThai || item.trang_thai || item.trangThai || "").trim().toUpperCase();
      return status === "ACTIVE";
    });

    // Chuẩn hóa mỗi item về shape dùng trong frontend
    productsData = activeOnly.map(item => ({
      id: item.id,
      title: item.tenSanPham || item.title || item.name,
      price: item.gia || item.price,
      description: item.moTa || item.description,
      anh: item.anh,        // raw path từ DB (vd '/images/products/xxx.jpg')
      image: item.anh || item.image || ""
    }));

    renderProducts();
  } catch (err) {
    console.error("Lỗi khi gọi API products:", err);
    const container = document.getElementById("products-container");
    if (container) container.innerHTML = `<p style="color: red;">Không tải được dữ liệu sản phẩm — ${err.message}</p>`;
  }

  console.log("productsData:", productsData);
  console.log("container:", document.getElementById("products-container"));
}

// chạy khi load
document.addEventListener("DOMContentLoaded", () => {
  fetchProducts();
});

/*==========================================*/


/*============ TEAPOTS ============*/
const TEAPOTS_API = API_BASE + "/api/teapots";
let teapotsData = [];
let teapotsShowAll = false;

function teapotCardHTML(p) {
  const imgSrc = buildImageUrl(p.image || p.anh || "");
  const title = escapeHtml(p.tenAmTra || p.title || "Ấm trà");
  const price = formatVND(p.gia || p.price);
  const id = p.id;

  const detailLink = `productTea.html?id=${id}`;

  return `
  <div class="product-card">

    <!-- CLICK ẢNH -->
    <a href="${detailLink}" class="product-link">
      <img src="${imgSrc}" alt="${title}" loading="lazy">
    </a>

    <div class="product-body">
      <div class="product-brand">Thanh Tâm Trà Quán</div>

      <!-- CLICK TÊN -->
      <a href="${detailLink}" class="product-link">
        <div class="product-name">${title}</div>
      </a>

      <div class="product-footer">
        <div class="product-price-red">${price}</div>

        <!-- NÚT + THÊM GIỎ -->
        <button class="add-btn"
          onclick='
            addToCart({
              id: ${id},
              name: "${title}",
              price: ${p.gia || p.price},
              image: "${p.image || p.anh}",
              qty: 1,
              type: "TEAPOT"
            });
            syncCartBadge();
            showAddToCartToast("Đã thêm ấm trà vào giỏ");
          '>
          +
        </button>
      </div>
    </div>
  </div>
  `;
}


function renderTeapots() {
  const container = document.getElementById("teapots-container");
  const btn = document.getElementById("view-more-teapots");

  if (!container) return;

  let toShow = teapotsData;
  if (!teapotsShowAll) toShow = teapotsData.slice(0, 3);

  container.innerHTML = toShow.map(p => teapotCardHTML(p)).join("");

  if (!btn) return;

  if (teapotsData.length <= 3) {
    btn.style.display = "none";
  } else {
    btn.style.display = "inline-block";
    btn.textContent = teapotsShowAll ? "Thu gọn" : "Xem thêm";
  }
}

function showMoreTeapots() {
  teapotsShowAll = !teapotsShowAll;
  renderTeapots();
}

async function fetchTeapots() {
  try {
    const res = await fetch(TEAPOTS_API);
    if (!res.ok) throw new Error("Không load được teapots");

    const arr = await res.json();

    teapotsData = arr.filter(item =>
      String(item.trangThai || "").toUpperCase() === "ACTIVE"
    );

    renderTeapots();

  } catch (err) {
    console.error("Teapots error:", err);
  }
}

// chạy khi load
document.addEventListener("DOMContentLoaded", fetchTeapots);
/*==========================================*/


// ================= CONTACT =================
async function fetchContact() {
  try {
    const res = await fetch(API_BASE + "/api/contact");
    if (!res.ok) throw new Error("Không load được contact");

    const data = await res.json();

    // ADDRESS
    const addrBox = document.getElementById("contact-address");
    addrBox.innerHTML = data.address
      .map(item => `<h3 class="contact-text">${item.noiDung}</h3>`)
      .join("");

    // EMAIL
    const emailBox = document.getElementById("contact-email");
    emailBox.innerHTML = data.email
      .map(item => `<h3 class="contact-text">${item.noiDung}</h3>`)
      .join("");

    // PHONE
    const phoneBox = document.getElementById("contact-phone");
    phoneBox.innerHTML = data.phone
      .map(item => `<h3 class="contact-text">${item.noiDung}</h3>`)
      .join("");

  } catch (err) {
    console.error("Contact error:", err);
  }
}

// chạy khi load trang
document.addEventListener("DOMContentLoaded", fetchContact);

/*==========================================*/


document.addEventListener("DOMContentLoaded", function () {
  const paymentMethod = document.getElementById("payment-method");
  const bankInfo = document.getElementById("bank-info");
  const momoInfo = document.getElementById("momo-info");

  if (!paymentMethod) return;

  bankInfo.style.display = "none";
  momoInfo.style.display = "none";

  paymentMethod.addEventListener("change", function () {
    if (this.value === "bank") {
      bankInfo.style.display = "flex";
      momoInfo.style.display = "none";
    } else if (this.value === "momo") {
      momoInfo.style.display = "flex";
      bankInfo.style.display = "none";
    } else {
      bankInfo.style.display = "none";
      momoInfo.style.display = "none";
    }
  });
});


// // ================= Xem giỏ hàng =================
// function getCart() {
//   return JSON.parse(localStorage.getItem("cart") || "[]");
// }

// function saveCart(cart) {
//   localStorage.setItem("cart", JSON.stringify(cart));
// }

// // ===== ADD TO CART =====
// function addToCart(product) {
//   let cart = getCart();
//   let found = cart.find(p => p.id === product.id);

//   if (found) {
//     found.qty += product.qty || 1;
//   } else {
//     cart.push({ ...product, qty: product.qty || 1 });
//   }

//   saveCart(cart);
//   alert("Đã thêm vào giỏ hàng!");
// }

// // ===== TOTAL PRICE =====
// function cartTotal() {
//   return getCart().reduce((sum, p) => sum + p.price * p.qty, 0);
// }

/*==========================================*/