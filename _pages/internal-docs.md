---
layout: page
title: Internal Documentation
permalink: /internal-docs/
description: Internal documentation that doesn't clutter the main navigation
nav: false
---

# Internal Documentation

This is an example of internal documentation that:
- **Doesn't appear in navigation** - keeps the main menu clean
- **Is accessible via direct link** - useful for team members or specific audiences
- **Can be referenced from other pages** - when needed

## Use Cases for Hidden Pages

### 1. **Work-in-Progress Content**
```yaml
---
layout: page
title: Draft Article
permalink: /drafts/new-research/
nav: false  # Hide until ready
---
```

### 2. **Special Landing Pages**
```yaml
---
layout: page
title: Conference Landing
permalink: /conference-2024/
nav: false  # Accessed via direct links only
---
```

### 3. **Archive Content**
```yaml
---
layout: page
title: Old Projects Archive
permalink: /archive/projects-2020/
nav: false  # Keep accessible but not prominent
---
```

### 4. **Internal Tools or Documentation**
```yaml
---
layout: page
title: Team Guidelines
permalink: /internal/guidelines/
nav: false  # For team members only
---
```

## Technical Details

The key is the `nav: false` parameter in the front matter:

```yaml
---
layout: page
title: Your Page Title
permalink: /your-url/
nav: false    # This is the magic line!
---
```

**Alternative approaches:**
- Simply omit the `nav` property entirely (defaults to false)
- Set `nav: true` and `nav_order: 999` to put it at the end if you want it barely visible

## Linking to Hidden Pages

You can link to hidden pages from anywhere:

- **From markdown:** `[Link text](/hidden-page/)`
- **With Jekyll variables:** `[Link text]({{ '/hidden-page/' | relative_url }})`
- **From HTML:** `<a href="{{ '/hidden-page/' | relative_url }}">Link text</a>`

## Benefits

✅ **Clean navigation** - Main menu stays focused  
✅ **SEO-friendly** - Pages are still indexed by search engines  
✅ **Flexible access** - Share direct links when needed  
✅ **Organized content** - Separate public vs. internal content  

---

*[← Back to main site]({{ '/' | relative_url }})*