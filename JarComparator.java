import java.util.zip.ZipFile;
import java.util.zip.ZipEntry;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.io.InputStream;
import java.io.IOException;
import java.util.Formatter;

public class JarComparator {

    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        String jarPath1 = "path_to_first_jar.jar";
        String jarPath2 = "path_to_second_jar.jar";

        Map<String, String> jar1Contents = getJarContents(jarPath1);
        Map<String, String> jar2Contents = getJarContents(jarPath2);

        Set<String> allFiles = new HashSet<>();
        allFiles.addAll(jar1Contents.keySet());
        allFiles.addAll(jar2Contents.keySet());

        for (String file : allFiles) {
            String hash1 = jar1Contents.get(file);
            String hash2 = jar2Contents.get(file);

            if (hash1 == null) {
                System.out.println(file + " was added.");
            } else if (hash2 == null) {
                System.out.println(file + " was removed.");
            } else if (!hash1.equals(hash2)) {
                System.out.println(file + " was modified.");
            }
        }
    }

    private static Map<String, String> getJarContents(String jarPath) throws IOException, NoSuchAlgorithmException {
        Map<String, String> fileHashes = new HashMap<>();
        ZipFile zipFile = new ZipFile(jarPath);

        try {
            zipFile.stream().forEach(zipEntry -> {
                if (!zipEntry.isDirectory()) {
                    try {
                        InputStream inputStream = zipFile.getInputStream(zipEntry);
                        String fileHash = getFileHash(inputStream);
                        fileHashes.put(zipEntry.getName(), fileHash);
                    } catch (IOException | NoSuchAlgorithmException e) {
                        e.printStackTrace();
                    }
                }
            });
        } finally {
            zipFile.close();
        }

        return fileHashes;
    }

    private static String getFileHash(InputStream inputStream) throws IOException, NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("MD5");
        byte[] buffer = new byte[1024];
        int bytesRead;

        while ((bytesRead = inputStream.read(buffer)) != -1) {
            digest.update(buffer, 0, bytesRead);
        }

        return byteArrayToHexString(digest.digest());
    }

    private static String byteArrayToHexString(byte[] bytes) {
        Formatter formatter = new Formatter();
        for (byte b : bytes) {
            formatter.format("%02x", b);
        }
        String result = formatter.toString();
        formatter.close();
        return result;
    }
}
