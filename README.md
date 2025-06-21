# 🏴‍☠️ PirateRate - Whitworth University Professor Reviews

A modern, beautiful Rate My Professor application specifically designed for Whitworth University students. Built with React, TypeScript, and styled with Whitworth University's official colors and the Pirates theme.

## ✨ Features

- **🏠 Beautiful Home Page** - Engaging hero section with animated pirate ship and Whitworth branding
- **🔍 Professor Search** - Find professors by name, department, or course
- **⭐ Detailed Reviews** - Comprehensive professor profiles with ratings, difficulty, and student feedback
- **📝 Review System** - Easy-to-use form for submitting professor reviews
- **📱 Responsive Design** - Works perfectly on desktop, tablet, and mobile devices
- **🎨 Whitworth Branding** - Official university colors and Pirates theme throughout

## 🎨 Design Features

- **Whitworth University Colors:**
  - Navy Blue (#1e3a8a)
  - Blue (#3b82f6)
  - Light Blue (#60a5fa)
  - Gold (#f59e0b)
  - Orange (#ea580c)

- **Pirates Theme:**
  - Pirate ship animations
  - Pirate emoji branding
  - Nautical color scheme
  - "PirateRate" branding

## 🚀 Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ratemyprofessor
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. **Open your browser:**
   Navigate to `http://localhost:3000` to view the application.

## 📁 Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── Header.tsx      # Navigation header with logo
│   └── Header.css      # Header styling
├── pages/              # Main application pages
│   ├── Home.tsx        # Landing page with hero section
│   ├── Home.css        # Home page styling
│   ├── ProfessorList.tsx # Professor search and listing
│   ├── ProfessorList.css # Professor list styling
│   ├── ProfessorDetail.tsx # Individual professor page
│   ├── ProfessorDetail.css # Professor detail styling
│   ├── AddReview.tsx   # Review submission form
│   └── AddReview.css   # Review form styling
├── App.tsx             # Main application component
├── App.css             # App-level styling
├── index.tsx           # Application entry point
└── index.css           # Global styles and CSS variables
```

## 🛠️ Built With

- **React 18** - Modern React with hooks and functional components
- **TypeScript** - Type-safe JavaScript development
- **React Router** - Client-side routing
- **Lucide React** - Beautiful, customizable icons
- **CSS3** - Custom styling with CSS variables and modern features

## 📱 Pages

### Home Page (`/`)
- Hero section with animated pirate ship
- Feature highlights
- Statistics showcase
- Call-to-action sections

### Professor List (`/professors`)
- Search functionality
- Department filtering
- Professor cards with ratings
- Responsive grid layout

### Professor Detail (`/professor/:id`)
- Detailed professor information
- Tabbed interface (Overview/Reviews)
- Rating breakdowns
- Student reviews with helpful voting

### Add Review (`/add-review/:professorId`)
- Comprehensive review form
- Star rating system
- Difficulty meter
- Form validation
- Character counting

## 🎯 Key Features

### Search & Filter
- Real-time search across professor names, departments, and courses
- Department-based filtering
- Responsive search interface

### Rating System
- 5-star rating system with visual feedback
- Difficulty level assessment (1-5 scale)
- "Would take again" percentage
- Overall rating calculations

### Review Management
- Anonymous review submissions
- Helpful/not helpful voting on reviews
- Character limits and validation
- Rich text formatting

### Responsive Design
- Mobile-first approach
- Tablet and desktop optimizations
- Touch-friendly interfaces
- Adaptive layouts

## 🔧 Development

### Available Scripts

- `npm start` - Runs the app in development mode
- `npm build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm eject` - Ejects from Create React App (one-way operation)

### Code Style

- TypeScript for type safety
- Functional components with hooks
- CSS modules for component styling
- Consistent naming conventions
- Responsive design patterns

## 🎨 Customization

### Colors
The application uses CSS custom properties for easy color customization. Main colors are defined in `src/index.css`:

```css
:root {
  --whitworth-navy: #1e3a8a;
  --whitworth-blue: #3b82f6;
  --whitworth-light-blue: #60a5fa;
  --whitworth-gold: #f59e0b;
  --whitworth-orange: #ea580c;
}
```

### Styling
- All components have their own CSS files
- Global styles are in `src/index.css`
- Utility classes are available for common patterns
- Responsive breakpoints are consistent throughout

## 🚀 Deployment

### Build for Production
```bash
npm run build
```

This creates an optimized production build in the `build` folder.

### Deploy Options
- **Netlify** - Drag and drop the `build` folder
- **Vercel** - Connect your GitHub repository
- **GitHub Pages** - Use the `gh-pages` package
- **AWS S3** - Upload the `build` folder to an S3 bucket

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Whitworth University** - For the inspiration and branding guidelines
- **React Community** - For the amazing ecosystem and tools
- **Lucide** - For the beautiful icon set
- **Create React App** - For the excellent development setup

## 📞 Support

For support, email support@piraterate.com or create an issue in the repository.

---

**🏴‍☠️ Go Pirates!** - Built with ❤️ for the Whitworth University community. 