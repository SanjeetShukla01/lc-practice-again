# Use Ubuntu as the base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    xfce4 xfce4-goodies \
    xrdp \
    firefox \
    x11vnc \
    xvfb \
    novnc \
    websockify \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up a VNC password
RUN mkdir -p ~/.vnc && \
    echo "mypassword" | vncpasswd -f > ~/.vnc/passwd && \
    chmod 600 ~/.vnc/passwd

# Expose ports for VNC and NoVNC
EXPOSE 5900 6080

# Set up VNC server and NoVNC
CMD ["sh", "-c", "Xvfb :0 -screen 0 1920x1080x24 & \
                   xfce4-session & \
                   x11vnc -forever -usepw -display :0 & \
                   websockify --web /usr/share/novnc/ 6080 localhost:5900"]
