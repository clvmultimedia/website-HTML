from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # cần cho flash thông báo

# Cấu hình gửi Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'clv.multimediaacademy@gmail.com'  # ✅ Gmail của bạn
app.config['MAIL_PASSWORD'] = 'xsoy jdov zpfc ffjd'               # ✅ Mật khẩu ứng dụng từ Google

mail = Mail(app)

# Route hiển thị form HTML
@app.route('/')
def index():
    return render_template('web clv.html')

# Route xử lý khi người dùng nhấn Gửi form
@app.route('/submit', methods=['POST'])
def submit():
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    course = request.form['course']
    message = request.form['message']

    # Soạn email gửi về cho trung tâm
    content = f"""
🔔 ĐĂNG KÝ MỚI:
Họ tên: {fullname}
SĐT: {phone}
Email: {email}
Khóa học: {course}
Ghi chú: {message}
"""

    try:
        msg = Message("📩 Đăng ký mới từ " + fullname,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['clv.multimediaacademy@gmail.com'],
                      body=content)
        mail.send(msg)
        flash('✅ Đăng ký thành công! Trung tâm sẽ liên hệ sớm.', 'success')
    except Exception as e:
        print("❌ LỖI KHI GỬI MAIL:", str(e))  # ⚠️ In lỗi ra màn hình terminal
        flash(f'❌ Gửi mail thất bại: {str(e)}', 'error')

    return redirect('/')

# Chạy Flask
if __name__ == '__main__':
    app.run(debug=True)
