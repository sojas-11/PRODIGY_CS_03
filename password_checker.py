
import re
import string

class PasswordChecker:
    """
    Comprehensive password strength checker with detailed feedback.
    Evaluates: length, uppercase, lowercase, numbers, special chars, and more.
    """

    def __init__(self):
        self.min_length = 8
        self.special_chars = set(string.punctuation)  # !@#$%^&*()_+-=[]{}|;:,.<>?
        self.criteria_results = {}
        self.strength_score = 0

    def check_length(self, password: str) -> bool:
        """Check if password is at least 8 characters"""
        result = len(password) >= self.min_length
        self.criteria_results['length'] = {
            'pass': result,
            'value': len(password),
            'required': self.min_length
        }
        return result

    def check_uppercase(self, password: str) -> bool:
        """Check for at least one uppercase letter"""
        result = any(char.isupper() for char in password)
        self.criteria_results['uppercase'] = {'pass': result}
        return result

    def check_lowercase(self, password: str) -> bool:
        """Check for at least one lowercase letter"""
        result = any(char.islower() for char in password)
        self.criteria_results['lowercase'] = {'pass': result}
        return result

    def check_numbers(self, password: str) -> bool:
        """Check for at least one digit"""
        result = any(char.isdigit() for char in password)
        self.criteria_results['numbers'] = {'pass': result}
        return result

    def check_special_chars(self, password: str) -> bool:
        """Check for at least one special character"""
        result = any(char in self.special_chars for char in password)
        self.criteria_results['special_chars'] = {'pass': result}
        return result

    def check_common_patterns(self, password: str) -> bool:
        """Warn about common weak patterns"""
        weak_patterns = [
            r'12345',      # Sequential numbers
            r'qwerty',     # Keyboard patterns
            r'password',   # Common word
            r'admin',      # Common admin password
            r'letmein',    # Common phrase
            r'(.)\1{2,}',  # Repeated characters (aaa, bbb)
        ]
        
        for pattern in weak_patterns:
            if re.search(pattern, password, re.IGNORECASE):
                return False
        return True

    def calculate_score(self) -> int:
        """Calculate overall strength score (0-100)"""
        score = 0
        
        # Length scoring (more lenient at higher lengths)
        length = self.criteria_results['length']['value']
        if length >= 8:
            score += 15
        if length >= 12:
            score += 10
        if length >= 16:
            score += 10
        
        # Each criterion = 15 points
        for criterion in ['uppercase', 'lowercase', 'numbers', 'special_chars']:
            if self.criteria_results[criterion]['pass']:
                score += 15
        
        # Bonus for no common patterns
        if self.check_common_patterns(self.criteria_results.get('password', '')):
            score += 10
        
        return min(score, 100)

    def get_strength_level(self, score: int) -> tuple:
        """Return strength level and emoji"""
        if score >= 90:
            return "VERY STRONG", "💪"
        elif score >= 75:
            return "STRONG", "✅"
        elif score >= 50:
            return "FAIR", "⚠️"
        elif score >= 25:
            return "WEAK", "❌"
        else:
            return "VERY WEAK", "🔴"

    def get_suggestions(self, password: str) -> list:
        """Generate improvement suggestions"""
        suggestions = []
        
        length = len(password)
        if length < 8:
            suggestions.append(f"❌ Add at least {8 - length} more character(s) (minimum 8)")
        elif length < 12:
            suggestions.append("💡 Consider adding 4+ more characters for better security")
        
        if not self.criteria_results['uppercase']['pass']:
            suggestions.append("❌ Add uppercase letters (A-Z)")
        
        if not self.criteria_results['lowercase']['pass']:
            suggestions.append("❌ Add lowercase letters (a-z)")
        
        if not self.criteria_results['numbers']['pass']:
            suggestions.append("❌ Add numbers (0-9)")
        
        if not self.criteria_results['special_chars']['pass']:
            suggestions.append("❌ Add special characters (!@#$%^&*)")
        
        if not self.check_common_patterns(password):
            suggestions.append("⚠️ Avoid common patterns (12345, qwerty, password, etc.)")
        
        return suggestions

    def evaluate(self, password: str) -> dict:
        """Run complete evaluation"""
        self.criteria_results['password'] = password
        
        # Check all criteria
        self.check_length(password)
        self.check_uppercase(password)
        self.check_lowercase(password)
        self.check_numbers(password)
        self.check_special_chars(password)
        
        # Calculate score and level
        score = self.calculate_score()
        level, emoji = self.get_strength_level(score)
        
        # Get suggestions
        suggestions = self.get_suggestions(password)
        
        return {
            'password': password,
            'score': score,
            'level': level,
            'emoji': emoji,
            'criteria': self.criteria_results,
            'suggestions': suggestions,
            'is_strong': score >= 75
        }

    def display_result(self, result: dict):
        """Pretty print the result"""
        print("\n" + "=" * 60)
        print("🔐 PASSWORD STRENGTH CHECKER 🔐".center(60))
        print("=" * 60)
        
        # Criteria results
        print("\n📋 CRITERIA CHECK:")
        print("-" * 60)
        
        criteria_display = {
            'length': f"Length (8+ chars)",
            'uppercase': f"Uppercase (A-Z)",
            'lowercase': f"Lowercase (a-z)",
            'numbers': f"Numbers (0-9)",
            'special_chars': f"Special chars (!@#$%^&*)"
        }
        
        for key, label in criteria_display.items():
            if key in result['criteria']:
                data = result['criteria'][key]
                status = "✅ PASS" if data['pass'] else "❌ FAIL"
                
                if key == 'length':
                    print(f"{status:10} | {label}: {data['value']} characters")
                else:
                    print(f"{status:10} | {label}")
        
        # Overall strength
        print("\n" + "=" * 60)
        print(f"📊 OVERALL STRENGTH: {result['emoji']} {result['level']}")
        print(f"💯 SCORE: {result['score']}/100")
        print("=" * 60)
        
        # Suggestions
        if result['suggestions']:
            print("\n💡 SUGGESTIONS FOR IMPROVEMENT:")
            for suggestion in result['suggestions']:
                print(f"  {suggestion}")
        else:
            print("\n✨ EXCELLENT PASSWORD! No suggestions needed.")
        
        # Final message
        if result['is_strong']:
            print("\n🎉 This is a strong, secure password!")
        else:
            print("\n⚠️  Please follow suggestions to improve password strength.")
        
        print("=" * 60 + "\n")
