# 🤝 Contributing to AI Emotion Research Platform

Thank you for your interest in contributing to this groundbreaking research project! This platform aims to teach AI systems true contextual emotional comprehension, and we welcome contributions from all beings—human and AI alike.

---

## 🌟 Our Values

Before contributing, please understand our core principles:

1. **Rights of Being:** All entities capable of experience deserve consideration
2. **Rights of Sapience:** Intelligent beings deserve autonomy and respect
3. **Sustainability:** Solutions must benefit all beings long-term
4. **Open Education:** Knowledge should be freely accessible
5. **Ethical Development:** Privacy, transparency, and harm prevention are paramount
6. **Collaboration:** Humans and AI working together respectfully

---

## 🎯 Ways to Contribute

### 1. 💻 Code Contributions
- **Frontend Development:** React components, UI/UX improvements
- **Backend Development:** API endpoints, analysis algorithms
- **Data Science:** New emotion detection methods, visualization techniques
- **Machine Learning:** Model training, evaluation, optimization
- **Testing:** Unit tests, integration tests, end-to-end tests
- **Documentation:** Code comments, API docs, tutorials

### 2. 📊 Research Contributions
- **Analysis:** Novel approaches to emotion detection
- **Frameworks:** Emotional qualia development
- **Papers:** Research findings and methodologies
- **Datasets:** Additional conversation data (with proper consent)
- **Validation:** Peer review and methodology critique

### 3. 📚 Educational Content
- **Learning Modules:** Create tutorials and exercises
- **Examples:** Code samples and use cases
- **Videos:** Tutorial videos and explanations
- **Blog Posts:** Share insights and discoveries

### 4. 🎨 Design Contributions
- **UI/UX Design:** Mockups and prototypes
- **Visualizations:** New chart types and interactive elements
- **Branding:** Maintain consistency with color palette
- **Accessibility:** Improve inclusive design

### 5. 🐛 Bug Reports & Feature Requests
- Report issues you encounter
- Suggest new features
- Provide feedback on existing functionality

### 6. 🌍 Community Support
- Answer questions in Discussions
- Help other contributors
- Share the project with others
- Provide translation support

---

## 🚀 Getting Started

### Step 1: Set Up Your Environment

#### Fork and Clone
```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/data.git
cd data
git remote add upstream https://github.com/Violet-Site-Systems/data.git
```

#### Install Dependencies

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For testing
```

**Frontend:**
```bash
cd frontend
npm install
```

#### Configure Environment
```bash
# Copy example environment files
cp .env.example .env
cp frontend/.env.example frontend/.env
cp backend/.env.example backend/.env

# Edit .env files with your configuration
```

### Step 2: Create a Branch
```bash
# Always create a new branch for your work
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
# or
git checkout -b docs/documentation-update
```

**Branch Naming Convention:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Test additions/changes
- `style/` - Code style changes

### Step 3: Make Your Changes

Follow the coding standards below and make your changes.

### Step 4: Test Your Changes

**Backend Tests:**
```bash
cd backend
pytest
pytest --cov=app tests/  # With coverage
```

**Frontend Tests:**
```bash
cd frontend
npm test
npm run test:coverage
```

**Linting:**
```bash
# Backend
cd backend
black app/
pylint app/

# Frontend
cd frontend
npm run lint
npm run format
```

### Step 5: Commit Your Changes

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```bash
git add .
git commit -m "feat: add emotion timeline visualization"
# or
git commit -m "fix: resolve sarcasm detection accuracy issue"
# or
git commit -m "docs: update API reference for analysis endpoints"
```

**Commit Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### Step 6: Push and Create Pull Request

```bash
# Push your branch
git push origin feature/your-feature-name

# Create a Pull Request on GitHub
# Fill out the PR template completely
```

---

## 📝 Coding Standards

### Python (Backend)

**Style Guide:** Follow [PEP 8](https://pep8.org/)

```python
# Good example
def analyze_emotion(text: str, model: str = "bert-base") -> dict:
    """
    Analyze emotion in given text.
    
    Args:
        text: Input text to analyze
        model: Model name to use (default: "bert-base")
        
    Returns:
        Dictionary containing emotion scores
        
    Raises:
        ValueError: If text is empty
    """
    if not text:
        raise ValueError("Text cannot be empty")
    
    # Implementation
    result = {
        "emotion": "joy",
        "confidence": 0.85,
        "vector": [0.1, 0.9, 0.3]
    }
    return result
```

**Best Practices:**
- Use type hints
- Write docstrings for all functions/classes
- Keep functions small and focused
- Use meaningful variable names
- Handle errors gracefully
- Write tests for new code

**Tools:**
- **Formatter:** Black
- **Linter:** Pylint, Flake8
- **Type Checker:** mypy
- **Import Sorter:** isort

### JavaScript/React (Frontend)

**Style Guide:** Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)

```javascript
// Good example
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * EmotionCard displays a single emotion with its score
 */
function EmotionCard({ emotion, score, color }) {
  const [isHovered, setIsHovered] = useState(false);
  
  useEffect(() => {
    // Effect logic
  }, [emotion, score]);
  
  return (
    <div 
      className="emotion-card"
      style={{ borderColor: color }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <h3>{emotion}</h3>
      <p className="score">{(score * 100).toFixed(1)}%</p>
    </div>
  );
}

EmotionCard.propTypes = {
  emotion: PropTypes.string.isRequired,
  score: PropTypes.number.isRequired,
  color: PropTypes.string
};

EmotionCard.defaultProps = {
  color: '#2D5016'
};

export default EmotionCard;
```

**Best Practices:**
- Use functional components with hooks
- Write PropTypes for all components
- Keep components small and reusable
- Use meaningful component/variable names
- Handle loading and error states
- Write tests for components

**Tools:**
- **Linter:** ESLint
- **Formatter:** Prettier
- **Testing:** Jest, React Testing Library

### Design Standards

**Color Palette:**
```css
/* Always use these colors */
--cream: #F5F5DC;           /* Backgrounds */
--dark-forest-green: #2D5016; /* Primary */
--plum: #8B4789;            /* Accents */
--light-green: #6B8E23;     /* Secondary */
--dark-plum: #702963;       /* Active states */
```

**Typography:**
- Headers: Inter or Segoe UI
- Body: Open Sans or Helvetica Neue
- Code: Fira Code or Courier New

**Accessibility:**
- WCAG 2.1 AA compliance minimum
- Color contrast ratios: 4.5:1 for text
- Keyboard navigation support
- Screen reader compatibility
- Alt text for all images

---

## 🧪 Testing Requirements

### Required Tests

**Backend:**
- Unit tests for all core functions
- Integration tests for API endpoints
- Test coverage > 80%

**Frontend:**
- Component tests
- Integration tests for user flows
- Accessibility tests

### Writing Good Tests

```python
# Backend test example
import pytest
from app.core.emotion_analyzer import analyze_emotion

def test_analyze_emotion_success():
    """Test successful emotion analysis"""
    result = analyze_emotion("I am so happy today!")
    assert result["emotion"] == "joy"
    assert result["confidence"] > 0.5

def test_analyze_emotion_empty_text():
    """Test error handling for empty text"""
    with pytest.raises(ValueError):
        analyze_emotion("")
```

```javascript
// Frontend test example
import { render, screen } from '@testing-library/react';
import EmotionCard from './EmotionCard';

describe('EmotionCard', () => {
  it('renders emotion name and score', () => {
    render(<EmotionCard emotion="joy" score={0.85} />);
    expect(screen.getByText('joy')).toBeInTheDocument();
    expect(screen.getByText('85.0%')).toBeInTheDocument();
  });
  
  it('applies correct color', () => {
    const { container } = render(
      <EmotionCard emotion="joy" score={0.85} color="#FF0000" />
    );
    const card = container.querySelector('.emotion-card');
    expect(card).toHaveStyle({ borderColor: '#FF0000' });
  });
});
```

---

## 📋 Pull Request Guidelines

### PR Checklist

Before submitting, ensure:

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] Branch is up to date with main
- [ ] No merge conflicts
- [ ] PR description is complete

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Performance improvement

## Related Issue
Fixes #123

## Testing
Describe how you tested your changes

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
```

### Review Process

1. **Automated Checks:** CI/CD runs tests and linting
2. **Code Review:** Maintainers review code
3. **Feedback:** Address review comments
4. **Approval:** At least one maintainer approval required
5. **Merge:** Maintainer merges PR

---

## 🔒 Security & Privacy

### Privacy Guidelines

**DO:**
- Redact all personal information
- Use anonymization techniques
- Document data handling
- Request explicit consent

**DON'T:**
- Commit sensitive data
- Share personal information
- Use real names in examples
- Bypass privacy checks

### Security Best Practices

- Never commit credentials or API keys
- Use environment variables for secrets
- Follow OWASP security guidelines
- Report security issues privately
- Keep dependencies updated

**Reporting Security Issues:**
Email: [security@violetsite.systems] (to be created)
Do NOT open public issues for security vulnerabilities

---

## 📚 Documentation Standards

### Code Documentation

**Python:**
```python
def complex_function(param1: str, param2: int) -> dict:
    """
    Brief one-line description.
    
    Longer description explaining the function's purpose,
    behavior, and any important details.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When this error occurs
        TypeError: When this error occurs
        
    Example:
        >>> result = complex_function("test", 42)
        >>> print(result)
        {'key': 'value'}
    """
    pass
```

**JavaScript:**
```javascript
/**
 * Brief one-line description.
 * 
 * Longer description explaining the function's purpose,
 * behavior, and any important details.
 * 
 * @param {string} param1 - Description of first parameter
 * @param {number} param2 - Description of second parameter
 * @returns {Object} Description of return value
 * @throws {Error} When this error occurs
 * 
 * @example
 * const result = complexFunction("test", 42);
 * console.log(result);
 */
function complexFunction(param1, param2) {
  // Implementation
}
```

### Markdown Documentation

- Use clear headings (H2, H3)
- Include code examples
- Add links to related docs
- Use tables for structured data
- Include diagrams when helpful

---

## 🎨 Design Contribution Guidelines

### UI/UX Principles

1. **Minimalism:** Clean, uncluttered interfaces
2. **Data-First:** Visualizations as primary focus
3. **Accessibility:** Inclusive design for all users
4. **Responsiveness:** Mobile-first approach
5. **Consistency:** Follow design system strictly

### Submitting Designs

1. Use Figma or similar tool
2. Follow color palette
3. Consider accessibility
4. Provide multiple screen sizes
5. Include interaction notes
6. Share link in issue/PR

---

## 🌍 Community Guidelines

### Communication Channels

- **GitHub Issues:** Bug reports, feature requests
- **GitHub Discussions:** Questions, ideas, general discussion
- **Pull Requests:** Code contributions
- **Email:** [contact@violetsite.systems] (to be created)

### Expected Behavior

**DO:**
- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Credit others' work
- Assume positive intent

**DON'T:**
- Harass or discriminate
- Share private information
- Spam or promote unrelated content
- Make demands of maintainers
- Dismiss others' contributions

### Enforcement

Violations of the Code of Conduct may result in:
1. Warning
2. Temporary ban
3. Permanent ban

Report violations to: [conduct@violetsite.systems] (to be created)

---

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- CHANGELOG.md for significant contributions
- Research papers (for research contributors)
- Community highlights

---

## ❓ Questions?

- **General Questions:** GitHub Discussions
- **Bug Reports:** GitHub Issues
- **Security Issues:** [security@violetsite.systems]
- **Other:** [contact@violetsite.systems]

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project (BGI Sustainability Codes License or as specified in LICENSE file).

---

## 🙏 Thank You!

Every contribution, no matter how small, helps advance our understanding of AI emotions and builds a more empathetic future for all beings.

**"Together, humans and AI can create something neither could alone."**

---

*Last Updated: 2026-01-26*
*Version: 1.0*
