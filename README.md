# Card Rewards Engine

A production-grade fintech platform that optimizes credit card selection based on spending patterns and product purchases. Uses AI agents for research, analysis, and recommendations.

## Features

- **Smart Card Matching**: AI-powered recommendations based on user spending patterns
- **Multi-Agent System**: Specialized agents for card research, product analysis, and recommendations
- **Real-time Scraping**: Selenium-based scrapers for credit cards and e-commerce platforms
- **Reward Optimization**: Intelligent reward calculation and comparison
- **Production-Ready**: Docker deployment, comprehensive testing, observability

## Tech Stack

- **Backend**: Python 3.11, FastAPI, PostgreSQL, SQLAlchemy
- **AI/ML**: LangChain, LangGraph, Composio
- **Web Scraping**: Selenium
- **Frontend**: React 18, TypeScript, Tailwind CSS
- **DevOps**: Docker, docker-compose, GitHub Actions
- **Observability**: Loguru, LangSmith

## Getting Started

### Prerequisites

- Docker & docker-compose
- Python 3.11+
- PostgreSQL 13+

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Prince1314-patel/card-rewards-engine.git
   cd card-rewards-engine
   ```

2. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start services**
   ```bash
   docker-compose up -d
   ```

4. **Run migrations**
   ```bash
   docker-compose exec api python -m alembic upgrade head
   ```

5. **Access the application**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - Frontend: http://localhost:3000

## Architecture

See [ARCHITECTURE.md](./docs/ARCHITECTURE.md) for detailed architecture documentation.

## API Documentation

See [API.md](./docs/API.md) for API reference.

## Deployment

See [DEPLOYMENT.md](./docs/DEPLOYMENT.md) for production deployment guide.

## Development

See [SETUP.md](./docs/SETUP.md) for development setup.

## Project Roadmap

1. **Phase 1**: Foundation & Structure ✅
2. **Phase 2**: Core Services (User, Card, Product, Reward Calculator)
3. **Phase 3**: Scrapers & Integrations (Amazon, Flipkart, Credit Card Sites)
4. **Phase 4**: AI Agents (Research, Analysis, Recommendation)
5. **Phase 5**: FastAPI Backend (REST API, WebSocket)
6. **Phase 6**: Testing (Unit, Integration, E2E)
7. **Phase 7**: React Frontend
8. **Phase 8**: Deployment & CI/CD
9. **Phase 9**: Public Release

## Testing

```bash
docker-compose exec api pytest -v --cov=app
```

## Contributing

Contributions are welcome! Please follow our git workflow:

1. Create feature branch from `dev`
2. Make changes and test
3. Create PR to `dev`
4. After approval, merge to `dev`
5. Periodic release to `main`

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Author

**Prince Patel** - ML/DL Engineer at Inexture Solutions

## Support

For issues, questions, or suggestions, please open an issue on GitHub.
