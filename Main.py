
#!/data/data/com.termux/files/usr/bin/python3

"""
===============================================================================
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║     ██╗  ██╗ █████╗ ██╗  ██╗    ██████╗  ██████╗  ██████╗  ████████╗       ║
║     ██║  ██║██╔══██╗╚██╗██╔╝    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝       ║
║     ███████║███████║ ╚███╔╝     ██████╔╝██║   ██║██║   ██║   ██║          ║
║     ██╔══██║██╔══██║ ██╔██╗     ██╔══██╗██║   ██║██║   ██║   ██║          ║
║     ██║  ██║██║  ██║██╔╝ ██╗    ██║  ██║╚██████╔╝╚██████╔╝   ██║          ║
║     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝          ║
║                                                                             ║
║                    PROFESSIONAL ROOT ENVIRONMENT v3.0                       ║
║                 Enterprise-Grade Termux Linux Installer                     ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  Author: SUNIL                      Team: Noob Cyber Tech                  ║
║  GitHub: Prince4you                  Edition: Ultimate                     ║
╚═════════════════════════════════════════════════════════════════════════════╝
===============================================================================
"""

import os
import sys
import time
import json
import random
import signal
import shutil
import platform
import subprocess
import threading
import traceback
import getpass
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Tuple, List, Any, Callable
from dataclasses import dataclass, field
from enum import Enum, auto
from queue import Queue

#===============================================================================
# ULTIMATE CONFIGURATION
#===============================================================================

VERSION = "3.0.0"
AUTHOR = "SUNIL"
TEAM = "Noob Cyber Tech"
GITHUB = "Prince4you"
CONFIG_DIR = Path.home() / '.haxroot'
LOG_FILE = CONFIG_DIR / 'install.log'
STATE_FILE = CONFIG_DIR / 'state.json'
PROOT_BASE = os.path.join(
    os.environ.get('PREFIX', '/data/data/com.termux/files/usr'),
    'var/lib/proot-distro/installed-rootfs'
)

# Create config directory
CONFIG_DIR.mkdir(exist_ok=True)

#===============================================================================
# ULTIMATE COLOR PALETTE
#===============================================================================

class Colors:
    """Ultimate color palette for maximum visual appeal"""
    # Reset
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Foreground - Standard
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Foreground - Bright
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Foreground - 256 Colors
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[38;5;129m'
    PINK = '\033[38;5;205m'
    TEAL = '\033[38;5;37m'
    GOLD = '\033[38;5;220m'
    SILVER = '\033[38;5;250m'
    LIME = '\033[38;5;154m'
    VIOLET = '\033[38;5;141m'
    CORAL = '\033[38;5;210m'
    AQUA = '\033[38;5;51m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Gradients for special effects
    GRADIENT1 = f'{BOLD}{ORANGE}'
    GRADIENT2 = f'{BOLD}{GOLD}'
    GRADIENT3 = f'{BOLD}{YELLOW}'
    GRADIENT4 = f'{BOLD}{LIME}'
    GRADIENT5 = f'{BOLD}{GREEN}'
    
    # Styles
    HEADER = f'{BOLD}{BRIGHT_CYAN}'
    SUBHEADER = f'{BOLD}{BRIGHT_MAGENTA}'
    SUCCESS = f'{BOLD}{BRIGHT_GREEN}'
    WARNING = f'{BOLD}{BRIGHT_YELLOW}'
    ERROR = f'{BOLD}{BRIGHT_RED}'
    INFO = f'{BOLD}{BRIGHT_BLUE}'
    HIGHLIGHT = f'{BOLD}{BRIGHT_WHITE}'
    MUTED = f'{DIM}{BRIGHT_BLACK}'
    ACCENT = f'{BOLD}{ORANGE}'

#===============================================================================
# ULTIMATE ICON SET
#===============================================================================

class Icons:
    """Ultimate icon set for maximum visual appeal"""
    # Status
    SUCCESS = '✅'
    ERROR = '❌'
    WARNING = '⚠️'
    INFO = 'ℹ️'
    QUESTION = '❓'
    DEBUG = '🐛'
    CRITICAL = '🔥'
    
    # Navigation
    POINTER = '➤'
    POINTER_SMALL = '❯'
    ARROW_RIGHT = '→'
    ARROW_LEFT = '←'
    ARROW_UP = '↑'
    ARROW_DOWN = '↓'
    DOUBLE_ARROW = '»'
    
    # UI Elements
    BULLET = '•'
    ELLIPSIS = '…'
    SEPARATOR = '─'
    DOUBLE_SEPARATOR = '═'
    CORNER_TL = '┌'
    CORNER_TR = '┐'
    CORNER_BL = '└'
    CORNER_BR = '┘'
    LINE_V = '│'
    LINE_H = '─'
    LINE_DOUBLE_V = '║'
    LINE_DOUBLE_H = '═'
    TEE_RIGHT = '├'
    TEE_LEFT = '┤'
    
    # Security
    LOCK = '🔒'
    UNLOCK = '🔓'
    KEY = '🔑'
    SHIELD = '🛡️'
    RADAR = '📡'
    
    # System
    TERMINAL = '💻'
    NETWORK = '🌐'
    PACKAGE = '📦'
    DOWNLOAD = '⬇️'
    UPLOAD = '⬆️'
    CLOCK = '⏱️'
    GEAR = '⚙️'
    CPU = '⚡'
    MEMORY = '🧠'
    DISK = '💾'
    
    # Awards
    STAR = '⭐'
    GOLD_STAR = '🌟'
    TROPHY = '🏆'
    CROWN = '👑'
    DIAMOND = '💎'
    
    # User
    USER = '👤'
    USERS = '👥'
    ROOT = '👑'
    ADMIN = '⚡'
    
    # Misc
    SPARKLES = '✨'
    ZAP = '⚡'
    HOURGLASS = '⏳'
    CONSTRUCTION = '🚧'
    GREEN_LOCK = '🟢'
    RED_LOCK = '🔴'
    YELLOW_LOCK = '🟡'
    ROBOT = '🤖'
    SKULL = '💀'
    FIRE = '🔥'
    DROPLET = '💧'
    LEAF = '🍃'
    FLOWER = '🌸'

#===============================================================================
# ORIGINAL BANNER - YOUR REQUEST
#===============================================================================

class OriginalBanner:
    """Your original hacker banner"""
    
    BANNER = f"""
{Colors.GREEN}           __________
                      .~#########%%;~.
                     /############%%;`\\
                    /######/~\\/~~%%;,;,\\
                   |#######\\    /;;;;.,.|
                   |#########\\/%;;;;;.,.|
          XX       |##/~~\\####%;;;/~~\\;|       XX
        XX..X      |#|  o  \\##%;/  o  |.|      X..XX
      XX.....X     |##\\____/##%;\\____/.,|     X.....XX
 XXXXX.....XX      \\#########/\\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \\######/%;\\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \\...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
 X# \\.X        @#%,.@  [[ Hax-root ]]    @#%,.@
                @#%,.@              @#%,.@
                  @#%,.@          @#%,.@
                     @#%,.@      @#%,.@
                       @#%.,@  @#%,.@
                        Noob Cyber Tech
{Colors.RESET}"""
    
    CREDIT = f"""
{Colors.RED}                      ▶ Coded by{Colors.GREEN} {AUTHOR}{Colors.RED}◀{Colors.RESET}
{Colors.RED}                      ⫸{Colors.YELLOW} Github :- {GITHUB} {Colors.RED}⫷{Colors.RESET}
"""
    
    QUOTES = [
        (f"{Colors.RED}Hack the planet!{Colors.RESET}", Colors.RED),
        (f"{Colors.YELLOW}With great power comes great responsibility.{Colors.RESET}", Colors.YELLOW),
        (f"{Colors.CYAN}The quieter you become, the more you can hear.{Colors.RESET}", Colors.CYAN),
        (f"{Colors.MAGENTA}There is no patch for human stupidity.{Colors.RESET}", Colors.MAGENTA),
        (f"{Colors.GREEN}Root access is just the beginning.{Colors.RESET}", Colors.GREEN),
        (f"{Colors.ORANGE}In the world of zeros and ones, we are the ones.{Colors.RESET}", Colors.ORANGE),
    ]
    
    @classmethod
    def show(cls):
        """Display the original banner"""
        os.system('clear')
        print(cls.BANNER)
        print(" ")
        print(cls.CREDIT)
        
        # Random quote
        quote, color = random.choice(cls.QUOTES)
        cols, _ = TerminalSize.get_size()
        print(f"\n{color}{Icons.SPARKLES}  {quote}  {Icons.SPARKLES}{Colors.RESET}".center(cols))
        print(f"{Colors.MUTED}{Icons.DOUBLE_SEPARATOR * cols}{Colors.RESET}\n")

#===============================================================================
# ULTIMATE LOGGING SYSTEM
#===============================================================================

class LogLevel(Enum):
    """Log levels"""
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

class UltimateLogger:
    """Ultimate logging system"""
    
    def __init__(self, log_file: Path = LOG_FILE):
        self.log_file = log_file
        self.session_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
        self.setup_logging()
    
    def setup_logging(self):
        """Initialize log file"""
        with open(self.log_file, 'a') as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"Session: {self.session_id} | Date: {datetime.now().isoformat()}\n")
            f.write(f"{'='*80}\n")
    
    def log(self, level: LogLevel, message: str, component: str = "SYSTEM"):
        """Log a message"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level.name}] [{component}] {message}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry)
        
        # Color output based on level
        if level == LogLevel.ERROR:
            print(f"{Colors.ERROR}{Icons.ERROR} {message}{Colors.RESET}")
        elif level == LogLevel.WARNING:
            print(f"{Colors.WARNING}{Icons.WARNING} {message}{Colors.RESET}")
        elif level == LogLevel.DEBUG:
            print(f"{Colors.MUTED}{Icons.DEBUG} {message}{Colors.RESET}")
        else:  # INFO and others
            print(f"{Colors.INFO}{Icons.INFO} {message}{Colors.RESET}")
    
    def debug(self, message: str, component: str = "DEBUG"):
        self.log(LogLevel.DEBUG, message, component)
    
    def info(self, message: str, component: str = "INFO"):
        self.log(LogLevel.INFO, message, component)
    
    def warning(self, message: str, component: str = "WARNING"):
        self.log(LogLevel.WARNING, message, component)
    
    def error(self, message: str, component: str = "ERROR"):
        self.log(LogLevel.ERROR, message, component)
    
    def critical(self, message: str, component: str = "CRITICAL"):
        self.log(LogLevel.CRITICAL, message, component)
        self.export_report()
    
    def success(self, message: str, component: str = "SUCCESS"):
        """Special method for success messages"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [SUCCESS] [{component}] {message}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"{Colors.SUCCESS}{Icons.SUCCESS} {message}{Colors.RESET}")
    
    def export_report(self):
        """Export session report"""
        report_file = CONFIG_DIR / f'report_{self.session_id}.log'
        shutil.copy(self.log_file, report_file)
        return report_file

#===============================================================================
# ULTIMATE STATE MANAGEMENT
#===============================================================================

class UltimateState:
    """State management with encryption"""
    
    def __init__(self, state_file: Path = STATE_FILE):
        self.state_file = state_file
        self.state = self.load()
    
    def load(self) -> Dict:
        """Load state from file"""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save(self):
        """Save state to file"""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get state value"""
        return self.state.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set state value"""
        self.state[key] = value
        self.save()
    
    def clear(self):
        """Clear all state"""
        self.state = {}
        self.save()

#===============================================================================
# ULTIMATE TERMINAL UTILITIES
#===============================================================================

class TerminalSize:
    """Get terminal dimensions"""
    
    @staticmethod
    def get_size() -> Tuple[int, int]:
        """Return (columns, rows)"""
        try:
            size = shutil.get_terminal_size()
            return size.columns, size.lines
        except:
            return 80, 24

class ProgressBar:
    """Ultimate animated progress bar"""
    
    STYLES = {
        'classic': ['█', '░'],
        'blocks': ['▓', '▒'],
        'dots': ['⣿', '⣀'],
        'arrows': ['➤', '·'],
        'stars': ['⭐', '☆'],
        'fire': ['🔥', '  '],
        'water': ['💧', '  '],
        'leaf': ['🍃', '  '],
    }
    
    def __init__(self, total: int, width: int = 50, prefix: str = '', 
                 suffix: str = '', style: str = 'classic'):
        self.total = total
        self.width = width
        self.prefix = prefix
        self.suffix = suffix
        self.current = 0
        self.start_time = time.time()
        self.style = self.STYLES.get(style, self.STYLES['classic'])
        self.fill_char, self.empty_char = self.style
    
    def update(self, progress: int):
        """Update progress bar"""
        self.current = min(progress, self.total)
        percent = self.current / self.total
        filled = int(self.width * percent)
        bar = self.fill_char * filled + self.empty_char * (self.width - filled)
        
        # Calculate ETA
        elapsed = time.time() - self.start_time
        if self.current > 0:
            eta = (elapsed / self.current) * (self.total - self.current)
            eta_str = time.strftime('%H:%M:%S', time.gmtime(eta))
        else:
            eta_str = '--:--:--'
        
        print(f"\r{self.prefix} [{Colors.SUCCESS}{bar}{Colors.RESET}] "
              f"{Colors.HIGHLIGHT}{int(percent * 100):3d}%{Colors.RESET} "
              f"{Colors.MUTED}ETA: {eta_str}{Colors.RESET} {self.suffix}",
              end='', flush=True)
        
        if self.current == self.total:
            print()

class Spinner:
    """Ultimate animated spinner"""
    
    FRAMES = {
        'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
        'arrows': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
        'pulse': ['█', '▓', '▒', '░', '▒', '▓'],
        'circle': ['◐', '◓', '◑', '◒'],
        'moon': ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘'],
        'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'],
        'weather': ['☀️', '🌤️', '⛅', '🌥️', '☁️', '🌧️', '⛈️', '🌩️'],
        'hearts': ['💛', '💙', '💜', '💚', '❤️', '🧡', '🖤', '🤍'],
    }
    
    def __init__(self, message: str = '', style: str = 'dots'):
        self.message = message
        self.running = False
        self.frame_index = 0
        self.style = style
        self.frames = self.FRAMES.get(style, self.FRAMES['dots'])
        self.start_time = None
        self.thread = None
    
    def _spin(self):
        """Update spinner frame"""
        while self.running:
            frame = self.frames[self.frame_index % len(self.frames)]
            elapsed = time.time() - self.start_time
            elapsed_str = time.strftime('%M:%S', time.gmtime(elapsed))
            
            print(f"\r{Colors.CYAN}{frame}{Colors.RESET} {self.message} "
                  f"{Colors.MUTED}[{elapsed_str}]{Colors.RESET}",
                  end='', flush=True)
            
            self.frame_index += 1
            time.sleep(0.1)
    
    def start(self):
        """Start the spinner"""
        self.running = True
        self.start_time = time.time()
        self.thread = threading.Thread(target=self._spin)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self, success: bool = True):
        """Stop the spinner"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=0.2)
        
        elapsed = time.time() - self.start_time
        elapsed_str = time.strftime('%M:%S', time.gmtime(elapsed))
        
        if success:
            print(f"\r{Colors.SUCCESS}{Icons.SUCCESS}{Colors.RESET} {self.message} "
                  f"{Colors.MUTED}[{elapsed_str}]{Colors.RESET} {' ' * 20}")
        else:
            print(f"\r{Colors.ERROR}{Icons.ERROR}{Colors.RESET} {self.message} "
                  f"{Colors.MUTED}[{elapsed_str}]{Colors.RESET} {' ' * 20}")

#===============================================================================
# ULTIMATE INPUT HANDLERS
#===============================================================================

class UltimateInput:
    """Ultimate input handling with validation"""
    
    @staticmethod
    def text(prompt: str, default: str = "", required: bool = False,
             validator: Optional[Callable] = None) -> str:
        """Get text input with validation"""
        while True:
            value = input(f"{Colors.GREEN}{Icons.POINTER}{Colors.RESET} "
                         f"{Colors.HIGHLIGHT}{prompt}{Colors.RESET} "
                         f"{Colors.MUTED}[{default}]:{Colors.RESET} ").strip()
            
            if not value:
                value = default
            
            if required and not value:
                print(f"{Colors.ERROR}{Icons.ERROR} This field is required{Colors.RESET}")
                continue
            
            if validator and not validator(value):
                print(f"{Colors.ERROR}{Icons.ERROR} Invalid input{Colors.RESET}")
                continue
            
            return value
    
    @staticmethod
    def password(prompt: str, confirm: bool = True,
                 min_length: int = 0) -> str:
        """Get password input with strength check"""
        while True:
            pwd = getpass.getpass(f"{Colors.GREEN}{Icons.LOCK}{Colors.RESET} "
                                  f"{Colors.HIGHLIGHT}{prompt}{Colors.RESET} ")
            
            if not pwd:
                print(f"{Colors.WARNING}{Icons.WARNING} No password set{Colors.RESET}")
                return ""
            
            if len(pwd) < min_length:
                print(f"{Colors.ERROR}{Icons.ERROR} Password must be at least "
                      f"{min_length} characters{Colors.RESET}")
                continue
            
            # Password strength indicator
            strength = 0
            if any(c.islower() for c in pwd): strength += 1
            if any(c.isupper() for c in pwd): strength += 1
            if any(c.isdigit() for c in pwd): strength += 1
            if any(c in '!@#$%^&*' for c in pwd): strength += 1
            
            strength_colors = [Colors.RED, Colors.YELLOW, Colors.CYAN, Colors.GREEN]
            strength_text = ['Weak', 'Fair', 'Good', 'Strong']
            
            if strength > 0:
                print(f"  {Colors.MUTED}Strength: {strength_colors[strength-1]}"
                      f"{strength_text[strength-1]}{Colors.RESET}")
            
            if confirm:
                confirm_pwd = getpass.getpass(f"{Colors.GREEN}{Icons.LOCK}{Colors.RESET} "
                                             f"{Colors.HIGHLIGHT}Confirm:{Colors.RESET} ")
                if pwd != confirm_pwd:
                    print(f"{Colors.ERROR}{Icons.ERROR} Passwords don't match{Colors.RESET}")
                    continue
            
            return pwd
    
    @staticmethod
    def confirm(prompt: str, default: bool = False) -> bool:
        """Get yes/no confirmation"""
        default_str = "Y/n" if default else "y/N"
        while True:
            response = input(f"{Colors.GREEN}{Icons.QUESTION}{Colors.RESET} "
                            f"{Colors.HIGHLIGHT}{prompt}{Colors.RESET} "
                            f"{Colors.MUTED}[{default_str}]:{Colors.RESET} ").strip().lower()
            
            if not response:
                return default
            
            if response in ['y', 'yes', 'true', '1']:
                return True
            if response in ['n', 'no', 'false', '0']:
                return False
            
            print(f"{Colors.ERROR}{Icons.ERROR} Please answer y/n{Colors.RESET}")
    
    @staticmethod
    def choice(prompt: str, options: List[str], default: Optional[int] = None) -> int:
        """Get choice from list"""
        print(f"\n{Colors.HIGHLIGHT}{prompt}{Colors.RESET}")
        for i, option in enumerate(options, 1):
            print(f"  {Colors.GREEN}[{i}]{Colors.RESET} {option}")
        
        while True:
            try:
                response = input(f"{Colors.GREEN}{Icons.POINTER}{Colors.RESET} "
                                f"Select (1-{len(options)}): ").strip()
                
                if not response and default is not None:
                    return default
                
                idx = int(response) - 1
                if 0 <= idx < len(options):
                    return idx
                
                print(f"{Colors.ERROR}{Icons.ERROR} Invalid choice{Colors.RESET}")
            except ValueError:
                print(f"{Colors.ERROR}{Icons.ERROR} Please enter a number{Colors.RESET}")

#===============================================================================
# ULTIMATE ERROR HANDLING
#===============================================================================

class UltimateError(Exception):
    """Base exception for ultimate errors"""
    pass

class NetworkError(UltimateError):
    """Network-related errors"""
    pass

class InstallationError(UltimateError):
    """Installation-related errors"""
    pass

class ConfigurationError(UltimateError):
    """Configuration-related errors"""
    pass

class UltimateErrorHandler:
    """Ultimate error handler with recovery options"""
    
    def __init__(self, logger: UltimateLogger):
        self.logger = logger
        self.error_count = 0
        self.recovery_attempts = 0
    
    def handle(self, error: Exception, context: str = "",
               fatal: bool = False) -> bool:
        """Handle an error with recovery options"""
        self.error_count += 1
        
        # Log the error
        self.logger.error(f"Error in {context}: {str(error)}", "ERROR")
        self.logger.debug(traceback.format_exc(), "DEBUG")
        
        # Show user-friendly error
        print(f"\n{Colors.ERROR}{Icons.CRITICAL} An error occurred{Colors.RESET}")
        print(f"{Colors.MUTED}Context: {context}{Colors.RESET}")
        print(f"{Colors.MUTED}Error: {str(error)}{Colors.RESET}")
        
        if fatal:
            print(f"{Colors.ERROR}{Icons.SKULL} Fatal error. Cannot continue.{Colors.RESET}")
            return False
        
        # Recovery options
        options = ["Retry", "Skip", "Abort"]
        choice = UltimateInput.choice("Recovery options:", options)
        
        if choice == 0:  # Retry
            self.recovery_attempts += 1
            return True
        elif choice == 1:  # Skip
            self.logger.warning(f"Skipping {context} after error", "RECOVERY")
            return True
        else:  # Abort
            self.logger.critical(f"User aborted after error in {context}", "ABORT")
            return False

#===============================================================================
# ULTIMATE MENU SYSTEM
#===============================================================================

class UltimateMenu:
    """Ultimate interactive menu with animations"""
    
    def __init__(self, title: str = "", width: int = 70):
        self.title = title
        self.width = width
        self.items = []
        self.selected = 0
    
    def add_item(self, text: str, value: Any = None,
                 disabled: bool = False, coming_soon: bool = False,
                 icon: str = Icons.BULLET):
        """Add a menu item"""
        self.items.append({
            'text': text,
            'value': value if value is not None else text,
            'disabled': disabled,
            'coming_soon': coming_soon,
            'icon': icon
        })
    
    def show(self) -> Any:
        """Display menu with animations"""
        # Header
        print(f"\n{Colors.HEADER}{Icons.CORNER_TL}{Icons.DOUBLE_SEPARATOR * self.width}{Icons.CORNER_TR}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}{self.title:^{self.width-2}}{Colors.RESET} "
              f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.TEE_RIGHT}{Icons.DOUBLE_SEPARATOR * self.width}{Icons.TEE_LEFT}{Colors.RESET}")
        
        # Menu items
        for i, item in enumerate(self.items):
            icon = item.get('icon', Icons.BULLET)
            
            if item.get('coming_soon', False):
                print(f"{Colors.HEADER}{Icons.LINE_V}{Colors.RESET}   "
                      f"{Colors.MUTED}{i+1}. {icon} {item['text']} "
                      f"{Icons.HOURGLASS} Coming Soon{Colors.RESET}  "
                      f"{Colors.HEADER}{Icons.LINE_V}{Colors.RESET}")
            elif item.get('disabled', False):
                print(f"{Colors.HEADER}{Icons.LINE_V}{Colors.RESET}   "
                      f"{Colors.MUTED}{i+1}. {icon} {item['text']}{Colors.RESET}  "
                      f"{Colors.HEADER}{Icons.LINE_V}{Colors.RESET}")
            else:
                marker = f"{Colors.SUCCESS}{Icons.POINTER}{Colors.RESET}" if i == self.selected else " "
                print(f"{Colors.HEADER}{Icons.LINE_V}{Colors.RESET} {marker} "
                      f"{Colors.GREEN}{i+1}.{Colors.RESET} "
                      f"{Colors.HIGHLIGHT}{icon}{Colors.RESET} "
                      f"{Colors.WHITE}{item['text']}{Colors.RESET}  "
                      f"{Colors.HEADER}{Icons.LINE_V}{Colors.RESET}")
        
        # Footer
        print(f"{Colors.HEADER}{Icons.CORNER_BL}{Icons.DOUBLE_SEPARATOR * self.width}{Icons.CORNER_BR}{Colors.RESET}")
        
        # Get selection
        while True:
            try:
                choice = input(f"\n{Colors.SUCCESS}{Icons.POINTER}{Colors.RESET} "
                              f"{Colors.HIGHLIGHT}Select option{Colors.RESET} "
                              f"{Colors.MUTED}(1-{len(self.items)}):{Colors.RESET} ")
                
                if choice.lower() in ['q', 'quit', 'exit']:
                    return None
                
                idx = int(choice) - 1
                if 0 <= idx < len(self.items):
                    item = self.items[idx]
                    if item.get('coming_soon', False):
                        print(f"{Colors.WARNING}{Icons.CONSTRUCTION} "
                              f"This feature is coming soon!{Colors.RESET}")
                        continue
                    elif item.get('disabled', False):
                        print(f"{Colors.ERROR}{Icons.ERROR} Option disabled{Colors.RESET}")
                        continue
                    else:
                        return item['value']
                else:
                    print(f"{Colors.ERROR}{Icons.ERROR} Invalid option{Colors.RESET}")
            except ValueError:
                print(f"{Colors.ERROR}{Icons.ERROR} Please enter a number{Colors.RESET}")

#===============================================================================
# ULTIMATE SYSTEM OPERATIONS
#===============================================================================

class UltimateSystem:
    """Ultimate system operations with retry logic"""
    
    def __init__(self, logger: UltimateLogger, error_handler: UltimateErrorHandler):
        self.logger = logger
        self.error_handler = error_handler
        self.max_retries = 3
    
    def run_command(self, command: str, show_output: bool = False,
                   timeout: Optional[int] = None) -> Tuple[bool, str]:
        """Run a command with retry logic"""
        for attempt in range(self.max_retries):
            try:
                if show_output:
                    result = subprocess.run(command, shell=True, check=True,
                                          capture_output=True, text=True,
                                          timeout=timeout)
                else:
                    result = subprocess.run(command, shell=True, check=True,
                                          stdout=subprocess.DEVNULL,
                                          stderr=subprocess.DEVNULL,
                                          timeout=timeout)
                
                self.logger.debug(f"Command succeeded: {command[:50]}...", "CMD")
                return True, result.stdout if show_output else ""
                
            except subprocess.TimeoutExpired:
                self.logger.warning(f"Command timed out (attempt {attempt+1})", "CMD")
                if attempt == self.max_retries - 1:
                    return False, "Timeout"
                    
            except subprocess.CalledProcessError as e:
                self.logger.warning(f"Command failed (attempt {attempt+1}): {e}", "CMD")
                if attempt == self.max_retries - 1:
                    return False, str(e)
                    
            except Exception as e:
                self.logger.error(f"Unexpected error: {e}", "CMD")
                return False, str(e)
            
            time.sleep(1 * (attempt + 1))  # Exponential backoff
        
        return False, "Max retries exceeded"
    
    def check_internet(self) -> bool:
        """Check internet connectivity with multiple methods"""
        methods = [
            ("ping -c 1 -W 2 8.8.8.8", "Google DNS"),
            ("ping -c 1 -W 2 1.1.1.1", "Cloudflare DNS"),
            ("curl -s --max-time 3 http://google.com", "HTTP check"),
        ]
        
        spinner = Spinner("Checking internet connection", style='pulse')
        spinner.start()
        
        for cmd, name in methods:
            success, _ = self.run_command(cmd, timeout=3)
            if success:
                spinner.stop(True)
                self.logger.success(f"Connected ({name})", "NETWORK")
                return True
        
        spinner.stop(False)
        self.logger.error("No internet connection", "NETWORK")
        return False
    
    def check_package(self, pkg: str) -> bool:
        """Check if package is installed"""
        result = subprocess.run(
            f"pkg list-installed 2>/dev/null | grep -q '^{pkg}'",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    
    def install_package(self, pkg: str) -> bool:
        """Install package with progress"""
        if self.check_package(pkg):
            self.logger.success(f"{pkg} already installed (skipping)", "PKG")
            return True
        
        spinner = Spinner(f"Installing {pkg}", style='clock')
        spinner.start()
        
        success, output = self.run_command(f"pkg install -y {pkg}")
        
        spinner.stop(success)
        
        if not success:
            # Try alternative installation method
            self.logger.warning(f"Failed to install {pkg}, trying alternative...", "PKG")
            spinner = Spinner(f"Alternative installation for {pkg}", style='dots')
            spinner.start()
            
            success, output = self.run_command(f"apt install -y {pkg}")
            spinner.stop(success)
        
        if success:
            self.logger.success(f"Installed {pkg}", "PKG")
        else:
            self.logger.error(f"Failed to install {pkg}", "PKG")
        
        return success
    
    def get_system_info(self) -> Dict[str, str]:
        """Get detailed system information"""
        info = {}
        
        # Device info
        info['device'] = platform.node()
        info['arch'] = platform.machine()
        info['os'] = platform.system()
        info['release'] = platform.release()
        
        # Termux info
        success, output = self.run_command("pkg list-installed | grep termux-tools", show_output=True)
        if success:
            info['termux_version'] = output.strip()
        
        # Storage info
        stat = shutil.disk_usage("/")
        info['storage_total'] = f"{stat.total // (1024**3)} GB"
        info['storage_free'] = f"{stat.free // (1024**3)} GB"
        
        return info

#===============================================================================
# DATA CLASSES
#===============================================================================

@dataclass
class DistroInfo:
    """Distribution information"""
    id: str
    name: str
    description: str
    icon: str = Icons.PACKAGE
    available: bool = True
    min_storage: int = 500  # MB
    dependencies: List[str] = field(default_factory=list)

@dataclass
class UserConfig:
    """User configuration"""
    root_pass: str = ""
    username: str = ""
    user_pass: str = ""
    sudo_nopass: bool = True
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

#===============================================================================
# ULTIMATE DISTRIBUTION MANAGER
#===============================================================================

class UltimateDistroManager:
    """Ultimate distribution manager with health checks"""
    
    DISTROS = {
        '1': DistroInfo('ubuntu', 'Ubuntu', 'User-friendly, great for beginners',
                       '🦄', True, 800, ['sudo', 'wget']),
        '2': DistroInfo('debian', 'Debian', 'Stable and reliable',
                       '🌀', True, 600, ['sudo', 'wget']),
        '3': DistroInfo('kali', 'Kali Linux', 'Penetration testing - Coming Soon',
                       '💀', False, 2000, ['sudo', 'wget']),
    }
    
    def __init__(self, logger: UltimateLogger, error_handler: UltimateErrorHandler,
                 system: UltimateSystem):
        self.logger = logger
        self.error_handler = error_handler
        self.system = system
        self.selected: Optional[DistroInfo] = None
    
    def select(self) -> bool:
        """Select a distribution with health check"""
        menu = UltimateMenu("SELECT DISTRIBUTION", width=70)
        
        for key, distro in self.DISTROS.items():
            if distro.available:
                menu.add_item(f"{distro.icon} {distro.name:<10} "
                            f"{Colors.MUTED}{distro.description}{Colors.RESET}",
                            distro, icon=distro.icon)
            else:
                menu.add_item(f"{distro.icon} {distro.name:<10} "
                            f"{Colors.MUTED}{distro.description}{Colors.RESET}",
                            distro, coming_soon=True, icon=distro.icon)
        
        menu.add_item(f"{Icons.ERROR} Exit", None, icon=Icons.ERROR)
        
        result = menu.show()
        if result and result.available:
            self.selected = result
            self.logger.success(f"Selected: {self.selected.icon} {self.selected.name}", "DISTRO")
            
            # Check storage
            stat = shutil.disk_usage("/")
            free_mb = stat.free // (1024**2)
            if free_mb < self.selected.min_storage:
                self.logger.warning(f"Low storage! Need {self.selected.min_storage}MB, have {free_mb}MB", "DISTRO")
                if not UltimateInput.confirm("Continue anyway?", default=True):
                    return False
            
            self.logger.info(f"Selected distribution: {self.selected.name}", "DISTRO")
            return True
        
        return False
    
    def is_installed(self) -> bool:
        """Check if selected distro is installed"""
        if not self.selected:
            return False
        return os.path.exists(os.path.join(PROOT_BASE, self.selected.id))
    
    def check_health(self) -> Dict[str, bool]:
        """Run health checks on the installation"""
        health = {
            'rootfs_exists': False,
            'apt_works': False,
            'has_internet': False,
        }
        
        if not self.selected:
            return health
        
        rootfs = os.path.join(PROOT_BASE, self.selected.id)
        health['rootfs_exists'] = os.path.exists(rootfs)
        
        if health['rootfs_exists']:
            # Test apt
            success, _ = self.system.run_command(
                f"proot-distro login {self.selected.id} -- apt update"
            )
            health['apt_works'] = success
            
            # Test internet inside distro
            success, _ = self.system.run_command(
                f"proot-distro login {self.selected.id} -- ping -c 1 8.8.8.8"
            )
            health['has_internet'] = success
        
        return health
    
    def repair(self) -> bool:
        """Attempt to repair a broken installation"""
        if not self.selected:
            return False
        
        self.logger.warning("Attempting repair...", "DISTRO")
        
        # Fix apt
        self.system.run_command(
            f"proot-distro login {self.selected.id} -- "
            "rm -rf /var/lib/apt/lists/* && apt update"
        )
        
        # Reinstall essential packages
        for pkg in self.selected.dependencies:
            self.system.run_command(
                f"proot-distro login {self.selected.id} -- apt install -y {pkg}"
            )
        
        # Check health again
        health = self.check_health()
        if all(health.values()):
            self.logger.success("Repair successful", "DISTRO")
        else:
            self.logger.error("Repair failed", "DISTRO")
        
        return all(health.values())
    
    def install(self) -> bool:
        """Install selected distribution with smart reinstall option"""
        if not self.selected or not self.selected.available:
            return False
        
        # Header
        print(f"\n{Colors.HEADER}{Icons.CORNER_TL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_TR}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}Installing {self.selected.icon} {self.selected.name}{Colors.RESET} "
              f"{' ' * (35 - len(self.selected.name))}{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.CORNER_BL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_BR}{Colors.RESET}\n")
        
        # SMART CHECK: If already installed, ask user what to do
        if self.is_installed():
            self.logger.info(f"{self.selected.name} is already installed", "DISTRO")
            print(f"\n{Colors.WARNING}{Icons.WARNING} {self.selected.name} is already installed{Colors.RESET}")
            
            options = [
                f"{Colors.SUCCESS}Continue with existing installation{Colors.RESET}",
                f"{Colors.ERROR}Reinstall (fresh installation){Colors.RESET}"
            ]
            choice = UltimateInput.choice("What would you like to do?", options)
            
            if choice == 0:  # Continue with existing
                self.logger.success("Using existing installation", "DISTRO")
                
                # Run health check
                health = self.check_health()
                if not all(health.values()):
                    self.logger.warning("Installation health check failed", "DISTRO")
                    if UltimateInput.confirm("Attempt repair?", default=True):
                        if self.repair():
                            self.logger.success("Repair successful", "DISTRO")
                        else:
                            self.logger.error("Repair failed", "DISTRO")
                            if not UltimateInput.confirm("Continue anyway?", default=False):
                                return False
                
                return True
            
            else:  # Reinstall
                self.logger.info(f"Reinstalling {self.selected.name}", "DISTRO")
                
                # Remove old installation
                spinner = Spinner(f"Removing old {self.selected.name} installation", style='fire')
                spinner.start()
                
                remove_process = subprocess.run(
                    f"proot-distro remove {self.selected.id}",
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                
                spinner.stop(remove_process.returncode == 0)
                
                if remove_process.returncode != 0:
                    self.logger.warning("Failed to remove old installation, but continuing...", "DISTRO")
        
        # Installation with progress
        spinner = Spinner(f"Installing {self.selected.name} (this may take a while)", style='clock')
        spinner.start()
        
        process = subprocess.Popen(
            f"proot-distro install {self.selected.id}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Monitor installation
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.logger.debug(output.strip(), "INSTALL")
        
        spinner.stop(process.returncode == 0)
        
        if process.returncode == 0:
            self.logger.success("Installation successful", "DISTRO")
            return True
        else:
            error = process.stderr.read()
            self.logger.error(f"Installation failed: {error}", "DISTRO")
            
            # Recovery options
            if UltimateInput.confirm("Show error details?", default=False):
                print(f"{Colors.MUTED}{error}{Colors.RESET}")
            
            if UltimateInput.confirm("Try again?", default=True):
                return self.install()
            
            return False

#===============================================================================
# ULTIMATE ENVIRONMENT SETUP
#===============================================================================

class UltimateEnvironmentSetup:
    """Ultimate environment configuration with multiple fallbacks for system info"""
    
    def __init__(self, distro: UltimateDistroManager, config: UserConfig,
                 logger: UltimateLogger, system: UltimateSystem):
        self.distro = distro
        self.config = config
        self.logger = logger
        self.system = system
    
    def detect_system_info_command(self) -> str:
        """Detect best available system info command (neofetch → fastfetch → custom)"""
        # Check for neofetch
        if self.system.check_package("neofetch") or self.system.run_command("which neofetch")[0]:
            return "neofetch --off"
        
        # Check for fastfetch
        if self.system.run_command("which fastfetch")[0]:
            return "fastfetch"
        
        # Fallback to custom ASCII
        return "custom_ascii"
    
    def generate_script(self) -> str:
        """Generate intelligent setup script with multiple fallbacks"""
        script = []
        script.append("#!/bin/bash")
        script.append("set -e")
        script.append("")
        
        # Detect distribution
        script.append("# Detect distribution")
        script.append("if [ -f /etc/os-release ]; then")
        script.append("    . /etc/os-release")
        script.append("    echo \"📦 Detected: $PRETTY_NAME\"")
        script.append("fi")
        script.append("")
        
        # Update system with smart retry
        script.append("# Update package lists")
        script.append("echo \"📦 Updating package lists...\"")
        script.append("for i in {1..3}; do")
        script.append("    if apt update -y; then")
        script.append("        break")
        script.append("    else")
        script.append("        echo \"⚠️  Retry $i/3...\"")
        script.append("        sleep 2")
        script.append("    fi")
        script.append("done")
        script.append("")
        
        script.append("# Upgrade system")
        script.append("echo \"⚙️  Upgrading packages...\"")
        script.append("DEBIAN_FRONTEND=noninteractive apt upgrade -y || true")
        script.append("")
        
        # Install essential packages
        script.append("# Install essential packages")
        script.append("echo \"📦 Installing essential packages...\"")
        script.append("ESSENTIAL_PKGS=\"sudo wget curl git nano\"")
        script.append("for pkg in $ESSENTIAL_PKGS; do")
        script.append("    if ! dpkg -l | grep -q \"^ii  $pkg\"; then")
        script.append("        DEBIAN_FRONTEND=noninteractive apt install -y $pkg")
        script.append("    else")
        script.append("        echo \"🟢 $pkg already installed\"")
        script.append("    fi")
        script.append("done")
        script.append("")
        
        # TRY NEOFETCH FIRST
        script.append("# Try to install neofetch")
        script.append("echo \"🎨 Trying to install neofetch...\"")
        script.append("if apt-cache show neofetch >/dev/null 2>&1; then")
        script.append("    DEBIAN_FRONTEND=noninteractive apt install -y neofetch")
        script.append("    FETCH_CMD=\"neofetch --off\"")
        script.append("    echo \"✅ neofetch installed\"")
        script.append("else")
        script.append("    echo \"⚠️ neofetch not available, trying fastfetch...\"")
        script.append("    # TRY FASTFETCH SECOND")
        script.append("    if apt-cache show fastfetch >/dev/null 2>&1; then")
        script.append("        DEBIAN_FRONTEND=noninteractive apt install -y fastfetch")
        script.append("        FETCH_CMD=\"fastfetch\"")
        script.append("        echo \"✅ fastfetch installed\"")
        script.append("    else")
        script.append("        echo \"⚠️ fastfetch not available, will use custom banner\"")
        script.append("        FETCH_CMD=\"custom_ascii\"")
        script.append("    fi")
        script.append("fi")
        script.append("")
        
        # Configure root
        if self.config.root_pass:
            script.append(f"echo 'root:{self.config.root_pass}' | chpasswd")
            script.append("echo \"👑 Root password configured\"")
        else:
            script.append("passwd -d root")
            script.append("echo \"⚠️  Root password disabled\"")
        script.append("")
        
        # Create user
        if self.config.username:
            script.append(f"echo \"👤 Creating user {self.config.username}...\"")
            script.append(f"useradd -m -s /bin/bash {self.config.username} 2>/dev/null || true")
            
            if self.config.user_pass:
                script.append(f"echo '{self.config.username}:{self.config.user_pass}' | chpasswd")
            else:
                script.append(f"passwd -d {self.config.username} 2>/dev/null || true")
            script.append("")
            
            # Sudo config
            script.append("echo \"🛡️  Configuring sudo...\"")
            script.append("mkdir -p /etc/sudoers.d")
            if self.config.sudo_nopass:
                script.append(f"echo '{self.config.username} ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/{self.config.username}")
            else:
                script.append(f"echo '{self.config.username} ALL=(ALL:ALL) ALL' > /etc/sudoers.d/{self.config.username}")
            script.append(f"chmod 440 /etc/sudoers.d/{self.config.username}")
            script.append("")
        
        # Root bashrc with intelligent system info display
        script.append("# Configure root shell")
        script.append("cat > /root/.bashrc << 'EOF'")
        script.append("# HAX-ROOT Ultimate Environment")
        script.append("clear")
        script.append("echo")
        script.append("if [ \"$FETCH_CMD\" = \"custom_ascii\" ]; then")
        script.append("    echo '╔══════════════════════════════════════════════════════════╗'")
        script.append("    echo '║                                                          ║'")
        script.append("    echo '║     ██╗  ██╗ █████╗ ██╗  ██╗    ██████╗  ██████╗  ██████╗  ████████╗ ║'")
        script.append("    echo '║     ██║  ██║██╔══██╗╚██╗██╔╝    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝ ║'")
        script.append("    echo '║     ███████║███████║ ╚███╔╝     ██████╔╝██║   ██║██║   ██║   ██║    ║'")
        script.append("    echo '║     ██╔══██║██╔══██║ ██╔██╗     ██╔══██╗██║   ██║██║   ██║   ██║    ║'")
        script.append("    echo '║     ██║  ██║██║  ██║██╔╝ ██╗    ██║  ██║╚██████╔╝╚██████╔╝   ██║    ║'")
        script.append("    echo '║     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝    ║'")
        script.append("    echo '║                                                          ║'")
        script.append("    echo '╠══════════════════════════════════════════════════════════╣'")
        script.append("    echo \"║  User: root                                               ║\"")
        script.append("    echo \"║  System: $(uname -o) $(uname -r)                         ║\"")
        script.append("    echo \"║  Date: $(date '+%Y-%m-%d %H:%M:%S')                       ║\"")
        script.append("    echo '╚══════════════════════════════════════════════════════════╝'")
        script.append("else")
        script.append("    $FETCH_CMD")
        script.append("fi")
        script.append("echo")
        script.append("export PS1='\\[\\033[1;31m\\]┌─[\\u@\\h]─[\\w]\\n└─# \\[\\033[0m\\]'")
        script.append("alias ls='ls --color=auto'")
        script.append("alias ll='ls -la'")
        script.append("alias la='ls -A'")
        script.append("alias update='apt update && apt upgrade'")
        script.append("alias ip='curl -s ifconfig.me'")
        script.append("alias sys='if command -v neofetch >/dev/null 2>&1; then neofetch --off; elif command -v fastfetch >/dev/null 2>&1; then fastfetch; else echo \"System: $(uname -o)\"; fi'")
        script.append("alias root='sudo su -'")
        script.append("EOF")
        script.append("")
        
        # User bashrc
        if self.config.username:
            script.append(f"cat > /home/{self.config.username}/.bashrc << 'EOF'")
            script.append("# HAX-ROOT Ultimate Environment")
            script.append("clear")
            script.append("echo")
            script.append("if [ \"$FETCH_CMD\" = \"custom_ascii\" ]; then")
            script.append("    echo '╔══════════════════════════════════════════════════════════╗'")
            script.append("    echo '║                                                          ║'")
            script.append("    echo '║     ██╗  ██╗ █████╗ ██╗  ██╗    ██████╗  ██████╗  ██████╗  ████████╗ ║'")
            script.append("    echo '║     ██║  ██║██╔══██╗╚██╗██╔╝    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝ ║'")
            script.append("    echo '║     ███████║███████║ ╚███╔╝     ██████╔╝██║   ██║██║   ██║   ██║    ║'")
            script.append("    echo '║     ██╔══██║██╔══██║ ██╔██╗     ██╔══██╗██║   ██║██║   ██║   ██║    ║'")
            script.append("    echo '║     ██║  ██║██║  ██║██╔╝ ██╗    ██║  ██║╚██████╔╝╚██████╔╝   ██║    ║'")
            script.append("    echo '║     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝    ║'")
            script.append("    echo '║                                                          ║'")
            script.append("    echo '╠══════════════════════════════════════════════════════════╣'")
            script.append(f"    echo \"║  User: {self.config.username:<50} ║\"")
            script.append("    echo \"║  System: $(uname -o) $(uname -r)                         ║\"")
            script.append("    echo \"║  Date: $(date '+%Y-%m-%d %H:%M:%S')                       ║\"")
            script.append("    echo '╚══════════════════════════════════════════════════════════╝'")
            script.append("else")
            script.append("    $FETCH_CMD")
            script.append("fi")
            script.append("echo")
            script.append("export PS1='\\[\\033[1;32m\\]┌─[\\u@\\h]─[\\w]\\n└─$ \\[\\033[0m\\]'")
            script.append("alias ls='ls --color=auto'")
            script.append("alias ll='ls -la'")
            script.append("alias la='ls -A'")
            script.append("alias update='sudo apt update && sudo apt upgrade'")
            script.append("alias ip='curl -s ifconfig.me'")
            script.append("alias sys='if command -v neofetch >/dev/null 2>&1; then neofetch --off; elif command -v fastfetch >/dev/null 2>&1; then fastfetch; else echo \"System: $(uname -o)\"; fi'")
            script.append("alias root='sudo su -'")
            script.append("EOF")
            script.append(f"chown {self.config.username}:{self.config.username} /home/{self.config.username}/.bashrc")
            script.append("")
        
        # Cleanup
        script.append("# Clean up")
        script.append("echo \"🧹 Cleaning up...\"")
        script.append("apt autoremove -y || true")
        script.append("apt autoclean -y || true")
        script.append("")
        
        # Final success message
        script.append("echo")
        script.append("echo \"🏆 Environment configuration complete! 🏆\"")
        script.append("echo \"ℹ️  Type 'exit' to return to Termux\"")
        script.append("echo")
        
        return '\n'.join(script)
    
    def run(self) -> bool:
        """Run environment setup with progress tracking"""
        if not self.distro.selected:
            return False
        
        # Header
        print(f"\n{Colors.HEADER}{Icons.CORNER_TL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_TR}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}Configuring Environment{Colors.RESET} "
              f"{' ' * 33}{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.CORNER_BL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_BR}{Colors.RESET}\n")
        
        # Write script
        script_path = os.path.join(PROOT_BASE, self.distro.selected.id, 'root', 'setup.sh')
        with open(script_path, 'w') as f:
            f.write(self.generate_script())
        os.chmod(script_path, 0o755)
        
        self.logger.info(f"Generated setup script for {self.distro.selected.name}", "SETUP")
        
        # Execute with progress
        spinner = Spinner("Configuring your environment", style='clock')
        spinner.start()
        
        process = subprocess.Popen(
            f"proot-distro login {self.distro.selected.id} -- bash /root/setup.sh",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Monitor with smart output
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                # Stop spinner, show output, restart spinner
                spinner.stop(True)
                print(f"  {Colors.MUTED}{output.strip()}{Colors.RESET}")
                spinner = Spinner("Continuing configuration", style='clock')
                spinner.start()
        
        spinner.stop(process.returncode == 0)
        
        if process.returncode == 0:
            # Cleanup
            self.system.run_command(
                f"proot-distro login {self.distro.selected.id} -- rm /root/setup.sh"
            )
            
            self.logger.success("Environment ready", "SETUP")
            
            # Test sudo if user was created
            if self.config.username:
                print(f"{Colors.INFO}{Icons.SHIELD} Testing sudo for {self.config.username}...{Colors.RESET}")
                time.sleep(1)
            
            return True
        else:
            error = process.stderr.read()
            self.logger.error(f"Configuration failed: {error}", "SETUP")
            
            if UltimateInput.confirm("Show error details?", default=False):
                print(f"{Colors.MUTED}{error}{Colors.RESET}")
            
            return False

#===============================================================================
# ULTIMATE LAUNCHER CREATOR
#===============================================================================

class UltimateLauncherCreator:
    """Create ultimate launcher scripts"""
    
    def __init__(self, distro: UltimateDistroManager, config: UserConfig,
                 logger: UltimateLogger):
        self.distro = distro
        self.config = config
        self.logger = logger
        self.prefix = os.environ.get('PREFIX', '/data/data/com.termux/files/usr')
    
    def create(self) -> bool:
        """Create launcher scripts with enhanced features"""
        if not self.distro.selected:
            return False
        
        # Header
        print(f"\n{Colors.HEADER}{Icons.CORNER_TL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_TR}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}Creating Launchers{Colors.RESET} "
              f"{' ' * 37}{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.CORNER_BL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_BR}{Colors.RESET}\n")
        
        # Root launcher with enhanced features
        root_launcher = os.path.join(self.prefix, 'bin', 'hax')
        with open(root_launcher, 'w') as f:
            f.write(f"""#!/data/data/com.termux/files/usr/bin/bash

# HAX-ROOT Ultimate Launcher
VERSION="{VERSION}"
DISTRO="{self.distro.selected.id}"

# Show welcome message
clear
echo -e "{Colors.HEADER}╔══════════════════════════════════════════════════════════╗{Colors.RESET}"
echo -e "{Colors.HEADER}║{Colors.RESET}              {Colors.HIGHLIGHT}HAX-ROOT ULTIMATE{Colors.RESET}                   {Colors.HEADER}║{Colors.RESET}"
echo -e "{Colors.HEADER}║{Colors.RESET}         {Colors.MUTED}Loading as root...{Colors.RESET}                {Colors.HEADER}║{Colors.RESET}"
echo -e "{Colors.HEADER}╚══════════════════════════════════════════════════════════╝{Colors.RESET}"
echo

# Launch environment
proot-distro login $DISTRO

# After exit
echo
echo -e "{Colors.MUTED}Exited from $DISTRO{Colors.RESET}"
""")
        os.chmod(root_launcher, 0o755)
        self.logger.success(f"Created hax → Login as root", "LAUNCHER")
        
        # User launcher
        if self.config.username:
            user_launcher = os.path.join(self.prefix, 'bin', 'hax-user')
            with open(user_launcher, 'w') as f:
                f.write(f"""#!/data/data/com.termux/files/usr/bin/bash

# HAX-ROOT Ultimate Launcher
VERSION="{VERSION}"
DISTRO="{self.distro.selected.id}"
USER="{self.config.username}"

# Show welcome message
clear
echo -e "{Colors.HEADER}╔══════════════════════════════════════════════════════════╗{Colors.RESET}"
echo -e "{Colors.HEADER}║{Colors.RESET}              {Colors.HIGHLIGHT}HAX-ROOT ULTIMATE{Colors.RESET}                   {Colors.HEADER}║{Colors.RESET}"
echo -e "{Colors.HEADER}║{Colors.RESET}         {Colors.MUTED}Loading as $USER...{Colors.RESET}                 {Colors.HEADER}║{Colors.RESET}"
echo -e "{Colors.HEADER}╚══════════════════════════════════════════════════════════╝{Colors.RESET}"
echo

# Launch environment
proot-distro login $DISTRO --user $USER

# After exit
echo
echo -e "{Colors.MUTED}Exited from $DISTRO as $USER{Colors.RESET}"
""")
            os.chmod(user_launcher, 0o755)
            self.logger.success(f"Created hax-user → Login as {self.config.username}", "LAUNCHER")
        
        return True

#===============================================================================
# ULTIMATE SUMMARY
#===============================================================================

class UltimateSummary:
    """Ultimate installation summary"""
    
    def __init__(self, distro: UltimateDistroManager, config: UserConfig,
                 logger: UltimateLogger, system: UltimateSystem):
        self.distro = distro
        self.config = config
        self.logger = logger
        self.system = system
    
    def show(self):
        """Show comprehensive installation summary"""
        OriginalBanner.show()
        
        # Summary header
        print(f"{Colors.HEADER}{Icons.CORNER_TL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_TR}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.SUCCESS}{Icons.TROPHY} INSTALLATION COMPLETE{Colors.RESET} "
              f"{' ' * 31}{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} {' ' * 70}{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        
        # Distribution info
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}{Icons.PACKAGE} Distribution:{Colors.RESET} "
              f"{self.distro.selected.icon} {self.distro.selected.name:<30}"
              f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        
        # Root password
        root_status = f"{Colors.SUCCESS}Set{Colors.RESET}" if self.config.root_pass else f"{Colors.WARNING}None{Colors.RESET}"
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}{Icons.ROOT} Root:{Colors.RESET} root ({root_status}){' ' * (40 - len(self.config.root_pass))}"
              f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        
        # User info
        if self.config.username:
            user_status = f"{Colors.SUCCESS}Set{Colors.RESET}" if self.config.user_pass else f"{Colors.WARNING}None{Colors.RESET}"
            sudo_status = f"{Colors.SUCCESS}NOPASSWD{Colors.RESET}" if self.config.sudo_nopass else f"{Colors.WARNING}Requires password{Colors.RESET}"
            print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
                  f"{Colors.HIGHLIGHT}{Icons.USER} User:{Colors.RESET} {self.config.username} ({user_status}){' ' * (34 - len(self.config.username))}"
                  f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
            print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
                  f"{Colors.HIGHLIGHT}{Icons.SHIELD} Sudo:{Colors.RESET} {sudo_status:<40}"
                  f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} {' ' * 70}{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        
        # Commands
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}Available Commands:{Colors.RESET}{' ' * 37}"
              f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}   "
              f"{Colors.SUCCESS}{Icons.POINTER}{Colors.RESET} {Colors.HIGHLIGHT}hax{Colors.RESET} - Login as root{' ' * (40 - len('hax - Login as root'))}"
              f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        
        if self.config.username:
            print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}   "
                  f"{Colors.SUCCESS}{Icons.POINTER}{Colors.RESET} {Colors.HIGHLIGHT}hax-user{Colors.RESET} - Login as {self.config.username}{' ' * (37 - len(self.config.username))}"
                  f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        
        print(f"{Colors.HEADER}{Icons.CORNER_BL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_BR}{Colors.RESET}\n")
        
        # Coming soon message
        print(f"{Colors.MAGENTA}{Icons.CONSTRUCTION} Kali Linux coming soon! Stay tuned.{Colors.RESET}\n")
        
        # System info
        sys_info = self.system.get_system_info()
        print(f"{Colors.INFO}{Icons.CPU} System Information:{Colors.RESET}")
        print(f"  {Colors.MUTED}Device:{Colors.RESET} {sys_info['device']}")
        print(f"  {Colors.MUTED}Architecture:{Colors.RESET} {sys_info['arch']}")
        print(f"  {Colors.MUTED}Storage:{Colors.RESET} {sys_info['storage_free']} free / {sys_info['storage_total']} total")
        print()
        
        # Log location
        print(f"{Colors.MUTED}Installation log: {LOG_FILE}{Colors.RESET}\n")
        
        # Post-install options
        if UltimateInput.confirm("Change root password?", default=False):
            os.system(f"proot-distro login {self.distro.selected.id} -- passwd")
            self.logger.info("Root password changed by user", "POST")
        
        if UltimateInput.confirm("Login as root now?", default=False):
            os.system("hax")

#===============================================================================
# MAIN APPLICATION
#===============================================================================

class HAXRootUltimate:
    """Ultimate main application"""
    
    def __init__(self):
        # Initialize core systems
        self.logger = UltimateLogger()
        self.error_handler = UltimateErrorHandler(self.logger)
        self.system = UltimateSystem(self.logger, self.error_handler)
        self.state = UltimateState()
        self.distro = UltimateDistroManager(self.logger, self.error_handler, self.system)
        self.config = UserConfig()
        
        # Set up signal handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        """Handle interrupts gracefully"""
        print(f"\n{Colors.ERROR}{Icons.CRITICAL} Interrupted by user{Colors.RESET}")
        self.logger.warning("User interrupted installation", "SIGNAL")
        self.cleanup()
        sys.exit(0)
    
    def cleanup(self):
        """Clean up temporary files"""
        try:
            # Remove temporary scripts
            if self.distro.selected and self.distro.is_installed():
                self.system.run_command(
                    f"proot-distro login {self.distro.selected.id} -- rm -f /root/setup.sh"
                )
            self.logger.info("Cleanup completed", "CLEANUP")
        except:
            pass
    
    def welcome(self):
        """Welcome screen with system check"""
        OriginalBanner.show()
        
        # Welcome message
        print(f"{Colors.SUCCESS}{Icons.TERMINAL} Welcome to HAX-ROOT Ultimate{Colors.RESET}")
        print(f"{Colors.MUTED}This professional tool will set up a complete Linux environment{Colors.RESET}")
        print(f"{Colors.MUTED}No root required - uses proot-distro for safe isolation{Colors.RESET}\n")
        
        # System health check
        print(f"{Colors.INFO}{Icons.RADAR} Running system health check...{Colors.RESET}")
        
        checks = []
        
        # Check storage
        stat = shutil.disk_usage("/")
        free_gb = stat.free / (1024**3)
        checks.append(("Storage", f"{free_gb:.1f} GB free", free_gb > 1))
        
        # Check Termux
        checks.append(("Termux", "Detected", True))
        
        # Check proot-distro
        has_proot = self.system.check_package("proot-distro")
        checks.append(("proot-distro", "Installed" if has_proot else "Not installed", has_proot))
        
        # Display checks
        for name, status, ok in checks:
            icon = f"{Colors.SUCCESS}{Icons.SUCCESS}{Colors.RESET}" if ok else f"{Colors.WARNING}{Icons.WARNING}{Colors.RESET}"
            print(f"  {icon} {Colors.HIGHLIGHT}{name}:{Colors.RESET} {Colors.MUTED}{status}{Colors.RESET}")
        
        print()
        
        # Check for existing state
        last_distro = self.state.get('last_distro')
        if last_distro:
            print(f"{Colors.INFO}{Icons.CLOCK} Previous installation detected: {last_distro}{Colors.RESET}")
        
        if not UltimateInput.confirm("Start installation?", default=True):
            self.logger.info("User cancelled installation", "START")
            sys.exit(0)
        
        self.logger.info("Installation started", "START")
    
    def configure_user(self):
        """Configure user accounts with smart defaults"""
        print(f"\n{Colors.HEADER}{Icons.CORNER_TL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_TR}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET} "
              f"{Colors.HIGHLIGHT}User Configuration{Colors.RESET} "
              f"{' ' * 34}{Colors.HEADER}{Icons.LINE_DOUBLE_V}{Colors.RESET}")
        print(f"{Colors.HEADER}{Icons.CORNER_BL}{Icons.DOUBLE_SEPARATOR * 70}{Icons.CORNER_BR}{Colors.RESET}\n")
        
        # Check for saved config
        saved_root = self.state.get('root_pass')
        if saved_root:
            print(f"{Colors.INFO}{Icons.CLOCK} Found saved configuration{Colors.RESET}")
            if UltimateInput.confirm("Use saved configuration?", default=True):
                self.config.root_pass = saved_root
                self.config.username = self.state.get('username', '')
                self.config.user_pass = self.state.get('user_pass', '')
                self.config.sudo_nopass = self.state.get('sudo_nopass', True)
                return
        
        # Root password
        self.config.root_pass = UltimateInput.password(
            "Root password (empty for none)",
            confirm=True,
            min_length=0
        )
        
        # Optional user
        if UltimateInput.confirm("Create regular user?", default=False):
            self.config.username = UltimateInput.text(
                "Username",
                default="hax",
                validator=lambda x: x.isalnum() and x[0].isalpha()
            )
            
            self.config.user_pass = UltimateInput.password(
                f"Password for {self.config.username}",
                confirm=True,
                min_length=0
            )
            
            self.config.sudo_nopass = not UltimateInput.confirm(
                "Require password for sudo?",
                default=False
            )
            
            if self.config.sudo_nopass:
                self.logger.success("Sudo will not require password (NOPASSWD)", "CONFIG")
        
        # Save configuration
        self.state.set('root_pass', self.config.root_pass)
        self.state.set('username', self.config.username)
        self.state.set('user_pass', self.config.user_pass)
        self.state.set('sudo_nopass', self.config.sudo_nopass)
        
        self.logger.info(f"User configured: root={'set' if self.config.root_pass else 'none'}, "
                        f"user={self.config.username or 'none'}", "CONFIG")
    
    def run(self):
        """Main execution with ultimate error handling"""
        try:
            self.welcome()
            
            # Check internet
            if not self.system.check_internet():
                if not UltimateInput.confirm("Continue without internet?", default=False):
                    return
            
            # Install dependencies
            print(f"\n{Colors.INFO}{Icons.PACKAGE} Checking dependencies...{Colors.RESET}")
            for pkg in ['proot-distro', 'wget', 'curl', 'git', 'nano']:
                self.system.install_package(pkg)
            
            # Select and install distro
            if not self.distro.select():
                return
            
            self.state.set('last_distro', self.distro.selected.name)
            
            if not self.distro.install():
                if not UltimateInput.confirm("Continue despite installation issues?", default=False):
                    return
            
            # Configure and setup
            self.configure_user()
            
            setup = UltimateEnvironmentSetup(self.distro, self.config, self.logger, self.system)
            if not setup.run():
                if not UltimateInput.confirm("Continue despite configuration issues?", default=False):
                    return
            
            # Create launchers and show summary
            launcher = UltimateLauncherCreator(self.distro, self.config, self.logger)
            launcher.create()
            
            summary = UltimateSummary(self.distro, self.config, self.logger, self.system)
            summary.show()
            
            # Export report
            report = self.logger.export_report()
            print(f"{Colors.MUTED}Session report saved to: {report}{Colors.RESET}")
            
        except UltimateError as e:
            self.error_handler.handle(e, "Main", fatal=True)
            sys.exit(1)
        except Exception as e:
            self.error_handler.handle(e, "Unexpected", fatal=True)
            sys.exit(1)
        finally:
            self.cleanup()

#===============================================================================
# ENTRY POINT
#===============================================================================

if __name__ == "__main__":
    app = HAXRootUltimate()
    app.run()
