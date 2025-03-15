# Use a lightweight base image (Alpine Linux)
FROM alpine:latest

# Install necessary dependencies
RUN apk update && \
    apk add --no-cache \
    firefox \
    xvfb \
    x11vnc \
    fluxbox \
    xterm \
    bash \
    sudo \
    dbus \
    ttf-freefont \
    mesa-dri-gallium \
    mesa-egl \
    mesa-gl \
    mesa-gles \
    xf86-video-dummy \
    xauth \
    tigervnc  # Add tigervnc for vncpasswd

# Set up a new user (optional but recommended for security)
RUN adduser -D -u 1000 user && \
    echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Switch to the new user
USER user
WORKDIR /home/user

# Set up X11 and VNC
RUN mkdir -p /home/user/.vnc && \
    echo "fluxbox &" > /home/user/.vnc/xstartup && \
    chmod +x /home/user/.vnc/xstartup && \
    mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

# Set a VNC password (e.g., "password")
RUN echo "password" | vncpasswd -f > /home/user/.vnc/passwd && \
    chmod 600 /home/user/.vnc/passwd

# Expose VNC port (default: 5900)
EXPOSE 5900

# Set up environment variables
ENV DISPLAY=:1
ENV RESOLUTION=1280x720

# Start Xvfb, Fluxbox, and x11vnc
CMD Xvfb :1 -screen 0 ${RESOLUTION}x24 & \
    sleep 2 && \
    fluxbox & \
    x11vnc -display :1 -forever -usepw -shared -rfbport 5900 -passwd /home/user/.vnc/passwd & \
    firefox