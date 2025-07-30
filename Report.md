# Overthewire

## Project Overview and Background

This project entailed completing four security wargames on the OverTheWire platform:

1. Natas (34 levels): Web application security (SQLi/XSS/file inclusion)

2. Narnia (7 levels): Binary exploitation (buffer overflow/environment variable injection)

3. Krypton (7 levels): Cryptanalysis (ROT13/Vigenère/stream cipher)

4. Leviathan (7 levels): Linux privilege escalation (symlink abuse/session hijacking)

### Technical Context

According to the 2024 OWASP Top 10 Report, 75% of web vulnerabilities stem from input validation failures (Natas focus). MITRE ATT&CK framework confirms binary vulnerabilities (Narnia focus) remain primary APT entry points. This project validates core course concepts through practical exploitation.

## Key Achievements

### Natas: Web Exploitation

1. HTTP header injection (L4)
2. PHP session fixation (L18-19)
3. File upload bypass (L12-13)
4. Referrer attack (L4)

### Narnia: Binary Security

1. Custom shellcode (L1)
2. Stack offset calculation (L2/4)
3. Symlink privilege escape (L3)

### Krypton: Cryptanalysis

1. Vigenère known-plaintext (L4)
2. Stream cipher CPA (L6)

### Leviathan: System Security

1. Hardlink abuse (L2)
2. SUID exploitation (L5)
