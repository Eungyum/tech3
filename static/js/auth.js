// login.html
// 계정 문의하기 링크 클릭 시 모달 표시
document.getElementById('accountInquiryLink').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('accountInquiryModal').style.display = 'block';
});

// 닫기 버튼 클릭 시 모달 숨김
document.querySelector('#accountInquiryModal .close').addEventListener('click', function() {
    document.getElementById('accountInquiryModal').style.display = 'none';
});

// 모달 외부 클릭 시 모달 숨김
window.addEventListener('click', function(event) {
    const modal = document.getElementById('accountInquiryModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
});
