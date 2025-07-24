package org.nexko.mineLabSecurityTemplate120.security;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Hashage {

    public String hashString(String input) {
        try {
            // Crée une instance de MessageDigest pour SHA-256
            MessageDigest md = MessageDigest.getInstance("SHA-512");

            // Transforme l'entrée en bytes et calcule le hash
            byte[] hashBytes = md.digest(input.getBytes());

            // Convertit les bytes en hexadécimal
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1)
                    hexString.append('0');
                hexString.append(hex);
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e); // Ne devrait pas arriver avec un algo standard comme SHA-256
        }
    }
}
