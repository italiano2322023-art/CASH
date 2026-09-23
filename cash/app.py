-- 1. جدول إعدادات الشركة (Company Settings)
CREATE TABLE company_settings (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) DEFAULT 'اسم الشركة',
    logo_url TEXT DEFAULT '',
    season_title VARCHAR(255) DEFAULT 'خزينة المكتب',
    currency VARCHAR(50) DEFAULT 'ج.م'
);

-- 2. جدول المعاملات اليومية والأرشيف (Transactions & Daily Archive)
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL DEFAULT CURRENT_DATE, -- تاريخ اليومية للأرشيف
    type VARCHAR(10) CHECK (type IN ('in', 'out')), -- وارد أم منصرف
    amount NUMERIC(12, 2) NOT NULL,
    receipt_no VARCHAR(100),
    description TEXT,
    payment_method VARCHAR(50) DEFAULT 'cash', -- كاش، فودافون كاش، إنستا باي
    is_closed BOOLEAN DEFAULT FALSE, -- هل تم تقفيل اليومية وأرشفتها؟
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);