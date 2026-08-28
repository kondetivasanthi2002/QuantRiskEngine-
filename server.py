import http.server
import socketserver
import json
import unittest
import time
import math
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from config.settings import SystemConfig
from engine.black_scholes import BlackScholesPricer
from engine.var_calculator import VaRCalculatorEngine
from engine.order_matching import LimitOrderBookEngine
from compliance.pre_trade_risk import SEC15c3_5Engine

PORT = 8000

HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuantRiskEngine - Institutional Terminal</title>
    <style>
        :root {
            --bg-color: #090514;
            --card-bg: #130a24;
            --card-hover: #1b0e33;
            --border-color: #281447;
            --border-glow: rgba(147, 51, 234, 0.4);
            --primary-violet: #9333ea;
            --accent-purple: #a855f7;
            --light-purple: #f3e8ff;
            --accent-green: #10b981;
            --accent-pink: #ec4899;
            --accent-red: #f43f5e;
            --accent-cyan: #06b6d4;
            --accent-amber: #f59e0b;
            --text-primary: #f8fafc;
            --text-secondary: #c084fc;
            --text-muted: #94a3b8;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 24px;
        }
        .header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 20px; border-bottom: 1px solid var(--border-color); margin-bottom: 24px; }
        .logo-group { display: flex; align-items: center; gap: 14px; }
        .logo-icon { width: 46px; height: 46px; background: linear-gradient(135deg, var(--primary-violet), var(--accent-cyan)); border-radius: 12px; display: flex; align-items: center; justify-content: center; }
        .logo-icon svg { width: 24px; height: 24px; fill: #ffffff; }
        .title { font-size: 24px; font-weight: 800; color: #ffffff; }
        .subtitle { font-size: 13px; color: var(--text-secondary); }
        .badge { background-color: rgba(16, 185, 129, 0.15); color: var(--accent-green); padding: 6px 14px; border-radius: 9999px; font-size: 13px; font-weight: 700; }
        .grid-4 { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-bottom: 24px; }
        .card { background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 16px; padding: 22px; }
        .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
        .card-title { font-size: 13px; color: var(--text-secondary); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 10px; }
        .icon-badge { width: 32px; height: 32px; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; background: rgba(147, 51, 234, 0.2); }
        .icon-badge svg { width: 18px; height: 18px; fill: #ffffff; }
        .stat-value { font-size: 30px; font-weight: 800; color: #ffffff; margin-bottom: 6px; }
        .stat-desc { font-size: 13px; font-weight: 600; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo-group">
            <div class="logo-icon"><svg viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg></div>
            <div>
                <div class="title">QuantRiskEngine Terminal</div>
                <div class="subtitle">Enterprise Financial Risk & Quantitative Execution Platform</div>
            </div>
        </div>
        <span class="badge">MARKET OPEN</span>
    </div>
    <div class="grid-4">
        <div class="card">
            <div class="card-header"><div class="card-title"><span class="icon-badge"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg></span>Value-at-Risk (99% VaR)</div></div>
            <div class="stat-value">$450,250.00</div>
            <div class="stat-desc" style="color:var(--accent-green)">SEC 15c3-5 Max Limit: $2,000,000</div>
        </div>
        <div class="card">
            <div class="card-header"><div class="card-title"><span class="icon-badge"><svg viewBox="0 0 24 24"><path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/></svg></span>Daily Portfolio PnL</div></div>
            <div class="stat-value" style="color:var(--accent-green)">+$128,450.80</div>
            <div class="stat-desc" style="color:var(--accent-green)">▲ +2.45% Return | Sharpe: 2.84</div>
        </div>
    </div>
</body>
</html>
"""

class QuantRiskHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_DASHBOARD.encode("utf-8"))
        elif self.path == "/api/v1/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "HEALTHY", "system": "QuantRiskEngine"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

class ReuseAddrTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    with ReuseAddrTCPServer(("127.0.0.1", PORT), QuantRiskHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()
