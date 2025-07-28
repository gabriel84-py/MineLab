package org.nexko.mineLabSecurityTemplate120.security;

import static org.bukkit.Bukkit.getServer;

public class Serverip {

    public String getip() {
        String ipserver = getServer().getIp();
        if (ipserver.isEmpty()) {
            ipserver = "0.0.0.0";
        }
        return ipserver;
    }
}
