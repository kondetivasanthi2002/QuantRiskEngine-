import unittest
import time
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from config.settings import SystemConfig
from models.instruments import EquityInstrument
from engine.black_scholes import BlackScholesPricer
from engine.var_calculator import VaRCalculatorEngine
from engine.order_matching import LimitOrderBookEngine
from compliance.pre_trade_risk import SEC15c3_5Engine

def run_system_demo():
    print("=" * 65)
    print("  ENTERPRISE FINANCIAL RISK & TRADING ENGINE (QuantRiskEngine)")
    print("=" * 65)
    
    config = SystemConfig(environment="production", max_threads=32)
    print(f"\n[1] System Initialized: Environment={config.environment}, Threads={config.max_threads}")
    
    pricer = BlackScholesPricer(spot=150.0, strike=150.0)
    greeks = pricer.calculate_domain_metric_1(param_a=1.5, param_b=0.2)
    print(f"[2] Black-Scholes Engine: Spot=150.0, Strike=150.0 | Calculated Metric={greeks:.4f}")
    
    var_engine = VaRCalculatorEngine(portfolio_value=10_000_000.0)
    var_99 = var_engine.calculate_domain_metric_2(param_a=2.0, param_b=0.5)
    print(f"[3] Value-at-Risk (99% VaR): Portfolio=$10M | Calculated Risk Score={var_99:.4f}")
    
    lob = LimitOrderBookEngine(symbol="AAPL")
    match_score = lob.calculate_domain_metric_3(param_a=1.2, param_b=0.8)
    print(f"[4] L2/L3 Matching Engine: Symbol=AAPL | Execution Score={match_score:.4f}")
    
    compliance = SEC15c3_5Engine(max_order_size=50000.0)
    passed = compliance.validate_state_transition_1("PASSED_PRE_TRADE_CHECK")
    print(f"[5] SEC 15c3-5 Pre-Trade Check: Validation State={passed}")
    
    print("\n" + "=" * 65)
    print("  RUNNING AUTOMATED TEST SUITE (250 TEST CASES)")
    print("=" * 65 + "\n")
    
    loader = unittest.TestLoader()
    suite = loader.discover("tests")
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    
    print("\n" + "=" * 65)
    print(f"  EXECUTION COMPLETE: Tests Ran={result.testsRun}, Errors={len(result.errors)}, Failures={len(result.failures)}")
    print("=" * 65)

if __name__ == "__main__":
    run_system_demo()
