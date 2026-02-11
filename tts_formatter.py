#!/usr/bin/env python3
"""
TTS Text Formatter - Prepares text for speech synthesis
Follows user-defined rules for voice message preparation
"""

import re

def format_for_tts(text: str, language: str = "en") -> str:
    """
    Format text to be speech-friendly
    
    Args:
        text: Original text
        language: Language code (en, bg, etc.)
    
    Returns:
        Formatted text ready for TTS
    """
    
    # Universal transformations
    formatted = text
    
    # Convert Backend N1/N2 to spoken form
    formatted = re.sub(r'Backend N1', 'Backend number one', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'Backend N2', 'Backend number two', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'N1', 'number one', formatted)
    formatted = re.sub(r'N2', 'number two', formatted)
    
    # Convert IP addresses to spoken form
    formatted = re.sub(r'10\.4\.4\.87', 'ten dot four dot four dot eighty seven', formatted)
    formatted = re.sub(r'10\.4\.4\.21', 'ten dot four dot four dot twenty one', formatted)
    formatted = re.sub(r'10\.4\.4\.90', 'ten dot four dot four dot ninety', formatted)
    formatted = re.sub(r'10\.4\.4\.93', 'ten dot four dot four dot ninety three', formatted)
    formatted = re.sub(r'10\.4\.4\.3', 'ten dot four dot four dot three', formatted)
    
    # Convert ports
    formatted = re.sub(r':5601', 'colon five six zero one', formatted)
    formatted = re.sub(r':9200', 'colon nine two zero zero', formatted)
    formatted = re.sub(r':9300', 'colon nine three zero zero', formatted)
    formatted = re.sub(r':2050', 'colon two zero five zero', formatted)
    formatted = re.sub(r':6343', 'colon six three four three', formatted)
    formatted = re.sub(r':2332', 'colon two three three two', formatted)
    formatted = re.sub(r':8080', 'colon eight zero eight zero', formatted)
    formatted = re.sub(r':5050', 'colon five zero five zero', formatted)
    
    # Convert technical abbreviations
    formatted = re.sub(r'\bAPI\b', 'A P I', formatted)
    formatted = re.sub(r'\bHTTP\b', 'H T T P', formatted)
    formatted = re.sub(r'\bHTTPS\b', 'H T T P S', formatted)
    formatted = re.sub(r'\bSSL\b', 'S S L', formatted)
    formatted = re.sub(r'\bSSH\b', 'S S H', formatted)
    formatted = re.sub(r'\bUDP\b', 'U D P', formatted)
    formatted = re.sub(r'\bTCP\b', 'T C P', formatted)
    formatted = re.sub(r'\bES\b', 'E S', formatted)
    formatted = re.sub(r'\bELK\b', 'E L K', formatted)
    formatted = re.sub(r'\bILM\b', 'I L M', formatted)
    formatted = re.sub(r'\bTTS\b', 'T T S', formatted)
    formatted = re.sub(r'\bOOM\b', 'O O M', formatted)
    formatted = re.sub(r'\bRAM\b', 'R A M', formatted)
    formatted = re.sub(r'\bCPU\b', 'C P U', formatted)
    formatted = re.sub(r'\bSSD\b', 'S S D', formatted)
    formatted = re.sub(r'\bIP\b', 'I P', formatted)
    formatted = re.sub(r'\bJSON\b', 'JASON', formatted)
    formatted = re.sub(r'\bNDJSON\b', 'N D JASON', formatted)
    formatted = re.sub(r'\.ndjson', 'dot n d jason', formatted)
    
    # Convert dashed names to "dash" form
    formatted = re.sub(r'cisco-nexus-bix-backend2-1', 'cisco dash nexus dash bix dash backend two dash one', formatted)
    formatted = re.sub(r'cisco-nexus', 'cisco dash nexus', formatted)
    formatted = re.sub(r'juniper-bix-backend1-1', 'juniper dash bix dash backend one dash one', formatted)
    formatted = re.sub(r'unified-flow', 'unified dash flow', formatted)
    formatted = re.sub(r'flow-collector', 'flow collector', formatted)
    formatted = re.sub(r'docker-compose', 'docker compose', formatted)
    formatted = re.sub(r'netflow', 'net flow', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'sflow', 's flow', formatted, flags=re.IGNORECASE)
    
    # Convert field names with dots
    formatted = re.sub(r'device\.name', 'device dot name', formatted)
    formatted = re.sub(r'source\.ip', 'source dot i p', formatted)
    formatted = re.sub(r'destination\.ip', 'destination dot i p', formatted)
    formatted = re.sub(r'source\.port', 'source dot port', formatted)
    formatted = re.sub(r'destination\.port', 'destination dot port', formatted)
    formatted = re.sub(r'network\.type', 'network dot type', formatted)
    formatted = re.sub(r'network\.bytes', 'network dot bytes', formatted)
    formatted = re.sub(r'network\.packets', 'network dot packets', formatted)
    formatted = re.sub(r'network\.transport', 'network dot transport', formatted)
    formatted = re.sub(r'network\.direction', 'network dot direction', formatted)
    formatted = re.sub(r'network\.iana_number', 'network dot iana number', formatted)
    formatted = re.sub(r'source\.as\.number', 'source a s number', formatted)
    formatted = re.sub(r'destination\.as\.number', 'destination a s number', formatted)
    formatted = re.sub(r'\.git', 'dot git', formatted)
    
    # Convert sizes and times
    formatted = re.sub(r'4096x', 'forty ninety six times', formatted)
    formatted = re.sub(r'778MB', 'seven hundred seventy eight megabytes', formatted)
    formatted = re.sub(r'5m0s', 'five minutes', formatted)
    formatted = re.sub(r'300s', 'three hundred seconds', formatted)
    formatted = re.sub(r'100%', 'one hundred percent', formatted)
    formatted = re.sub(r'99%', 'ninety nine percent', formatted)
    formatted = re.sub(r'15m', 'fifteen minutes', formatted)
    formatted = re.sub(r'15s', 'fifteen seconds', formatted)
    
    # Convert file paths
    formatted = re.sub(r'/tmp/', 'slash tmp slash ', formatted)
    formatted = re.sub(r'/home/', 'slash home slash ', formatted)
    formatted = re.sub(r'/etc/', 'slash etc slash ', formatted)
    formatted = re.sub(r'/var/', 'slash var slash ', formatted)
    formatted = re.sub(r'/opt/', 'slash opt slash ', formatted)
    formatted = re.sub(r'/usr/', 'slash usr slash ', formatted)
    formatted = re.sub(r'_export', 'underscore export', formatted)
    formatted = re.sub(r'_import', 'underscore import', formatted)
    formatted = re.sub(r'_find', 'underscore find', formatted)
    formatted = re.sub(r'\.conf', 'dot conf', formatted)
    formatted = re.sub(r'\.yml', 'dot yml', formatted)
    formatted = re.sub(r'\.json', 'dot json', formatted)
    formatted = re.sub(r'\.sh', 'dot sh', formatted)
    formatted = re.sub(r'\.py', 'dot py', formatted)
    
    # Language-specific transformations
    if language == "bg":
        formatted = apply_bulgarian_rules(formatted)
    
    return formatted

def apply_bulgarian_rules(text: str) -> str:
    """Apply Bulgarian-specific TTS formatting"""
    
    formatted = text
    
    # Use Bulgarian-friendly name (NO dash - user preference)
    formatted = re.sub(r'Valentin-bot', 'Валентин бот', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'Валентин-бот', 'Валентин бот', formatted)
    
    # Make friendly additions
    if not formatted.startswith('Здравей') and not formatted.startswith('Хей'):
        formatted = 'Здравей! ' + formatted
    
    # Convert English technical terms to Bulgarian phonetics
    formatted = re.sub(r'\bbackend\b', 'бекенд', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bfrontend\b', 'фронтенд', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bdashboard\b', 'дашборд', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bdocker\b', 'докър', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\belasticsearch\b', 'еластик сърч', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\blogstash\b', 'логсташ', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bkibana\b', 'кибана', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bcontainer\b', 'контейнър', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bserver\b', 'сървър', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bconfig\b', 'конфигурация', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\berror\b', 'грешка', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bnetwork\b', 'мрежа', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bdevice\b', 'устройство', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\brouter\b', 'рутер', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bswitch\b', 'суич', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bflow\b', 'флоу', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bdata\b', 'данни', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bdisk\b', 'диск', formatted, flags=re.IGNORECASE)
    formatted = re.sub(r'\bmemory\b', 'памет', formatted, flags=re.IGNORECASE)
    
    # Convert numbers to Bulgarian words when appropriate
    # (Keep N1/N2 as converted earlier)
    
    return formatted


def format_bulgarian_introduction(name: str = "Виктор") -> str:
    """Generate a friendly Bulgarian introduction"""
    
    text = f"""Здравей, {name}! Аз съм Валентин-тире-бот, твоят виртуален асистент. 
    Говоря български език и съм готов да ти помогна с всичко, от което се нуждаеш. 
    Разбирам от мрежи, системи и всякакви технически неща. 
    Ако искаш нещо, просто попитай!"""
    
    return format_for_tts(text, language="bg")


if __name__ == "__main__":
    # Test the formatter
    test_text = "Backend N2 (10.4.4.90) containers crashed. cisco-nexus-bix-backend2-1 device.name field updated."
    
    print("Original:")
    print(test_text)
    print("\nEnglish TTS:")
    print(format_for_tts(test_text, "en"))
    print("\nBulgarian TTS:")
    print(format_for_tts(test_text, "bg"))
