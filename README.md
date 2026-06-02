# Sentiment Analysis Web App

A modern, beautiful web application for analyzing the emotional tone of text using TextBlob and Django. Powered by a professional UI with gradient design and smooth animations.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Django](https://img.shields.io/badge/Django-6.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

- **Real-time Sentiment Analysis** - Analyze text instantly with polarity and subjectivity scores
- **Modern UI** - Beautiful gradient design with smooth animations
- **1-10 Scale Scoring** - Easy-to-understand sentiment scores from 1 to 10
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Visual Feedback** - Progress bars, emojis, and color-coded results
- **Production Ready** - Deployed with Gunicorn and WhiteNoise

## 📊 Analysis Metrics

- **Polarity Score (1-10):** Measures how positive/negative the text is
  - 1 = Very Negative
  - 5.5 = Neutral
  - 10 = Very Positive

- **Subjectivity Score (1-10):** Measures how subjective/objective the text is
  - 1 = Very Objective
  - 10 = Very Subjective

## 🚀 Live Demo

**[🌐 Visit Live App](https://sentiment-analysis-gemb.onrender.com/)**

Try the sentiment analysis tool now! No installation needed.

## 📋 Tech Stack

- **Backend:** Django 6.0+
- **NLP:** TextBlob
- **Frontend:** Modern CSS with Gradient Design
- **Icons:** Font Awesome 6
- **Server:** Gunicorn
- **Static Files:** WhiteNoise
- **Deployment:** Render.com

## 🛠️ Installation

### Prerequisites

- Python 3.9+
- pip (Python package manager)

### Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/AchutaKumar/sentiment-analysis.git
cd sentiment-analysis
```

2. **Create and activate virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Start development server:**
```bash
python manage.py runserver
```

6. **Open in browser:**
```
http://127.0.0.1:8000
```

## 📁 Project Structure

```
sentiment-analysis/
├── sentiment_project/
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── sentiment_app/
│   ├── views.py             # Sentiment analysis logic
│   ├── urls.py              # App URLs
│   ├── models.py            # Database models
│   └── static/
│       └── css/
│           └── style.css    # Modern UI styles
├── templates/
│   └── index.html           # Main template
├── requirements.txt         # Python dependencies
├── render.yaml              # Render.com configuration
├── build.sh                 # Build script
├── start.sh                 # Start script
└── manage.py                # Django management script
```

## 🎨 UI Features

- **Gradient Background** - Beautiful purple-to-pink gradient
- **Animated Cards** - Smooth entrance animations
- **Color-Coded Results:**
  - 🟢 Green for Positive sentiment
  - 🔴 Red for Negative sentiment
  - 🟡 Orange for Neutral sentiment
- **Progress Bars** - Visual representation of scores
- **Responsive Breakpoints:**
  - Desktop: Full layout
  - Tablet (768px): Optimized spacing
  - Mobile (480px): Compact design

## 🚀 Deployment

### Deploy on Render.com

1. **Sign up at [Render.com](https://render.com)**
2. **Connect your GitHub repository**
3. **Create new Web Service**
4. **Configuration will auto-load from `render.yaml`**
5. **Click Deploy**

Your app will be live in 2-3 minutes!

**Build Command:**
```
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

**Start Command:**
```
gunicorn sentiment_project.wsgi:application
```


## 📦 Dependencies

```
Django==6.0.0
TextBlob==0.17.1
gunicorn==26.0.0
whitenoise==6.12.0
NLTK==3.8.1
```

## 🔧 Configuration

### Django Settings

**For Development:**
```python
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

**For Production:**
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', '*.onrender.com']
```

The app automatically detects environment using the `DEBUG` environment variable.

## 📝 Usage

1. **Enter Text:** Type or paste any text in the textarea
2. **Click Analyze:** Press the "Analyze Sentiment" button
3. **View Results:**
   - See emoji indicator (😊 😞 😐)
   - Read sentiment label (Positive/Negative/Neutral)
   - Check polarity and subjectivity scores
   - View progress bars for visual representation

## 🎯 Example

**Input:** "I absolutely love this product! It's amazing and works perfectly!"

**Output:**
- Sentiment: **Positive 😊**
- Polarity Score: **8.5/10**
- Subjectivity Score: **7.2/10**

## 🔐 Security Notes

- `SECRET_KEY` should be changed for production
- Use environment variables for sensitive data
- Set `DEBUG = False` on production
- Update `ALLOWED_HOSTS` with your domain

## 🐛 Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Issues
```bash
python manage.py migrate
python manage.py makemigrations
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Create pull requests

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details

## 👤 Author

**Achuta Kumar**
- GitHub: [@AchutaKumar](https://github.com/AchutaKumar)
- Email: your-email@example.com


